"""
Tests for the Validator Agent — 3-Tier Validation Engine
"""
from django.test import TestCase
from .validator_agent import ValidatorAgent, ValidationReport, ValidationIssue
from .migration_context import MigrationContext


class ValidatorTier1Tests(TestCase):
    """Test Tier 1: Static Validation"""

    def setUp(self):
        self.validator = ValidatorAgent()

    def test_valid_python_passes_syntax_check(self):
        """Valid Python code should pass syntax check"""
        code = "from django.urls import path\nx = 1 + 2\n"
        report = self.validator.validate_file("test.py", "", code)
        syntax_errors = [i for i in report.issues if i.category == "syntax"]
        self.assertEqual(len(syntax_errors), 0)

    def test_invalid_python_fails_syntax_check(self):
        """Broken Python should be caught as syntax error"""
        code = "def foo(\n  x = 1\n"
        report = self.validator.validate_file("test.py", "", code)
        syntax_errors = [i for i in report.issues if i.category == "syntax"]
        self.assertGreater(len(syntax_errors), 0)
        self.assertFalse(report.passed)

    def test_deprecated_import_detected(self):
        """django.conf.urls.url should be flagged"""
        code = "from django.conf.urls import url\nurlpatterns = []\n"
        report = self.validator.validate_file("urls.py", "", code)
        import_errors = [i for i in report.issues if i.category == "import"]
        self.assertGreater(len(import_errors), 0)
        self.assertIn("Deprecated import", import_errors[0].message)

    def test_modern_import_passes(self):
        """django.urls.path should NOT be flagged"""
        code = "from django.urls import path\nurlpatterns = []\n"
        report = self.validator.validate_file("urls.py", "", code)
        import_errors = [i for i in report.issues if i.category == "import"]
        self.assertEqual(len(import_errors), 0)

    def test_deprecated_ugettext_detected(self):
        """ugettext_lazy should be flagged as deprecated"""
        code = "from django.utils.translation import ugettext_lazy as _\nx = _('hello')\n"
        report = self.validator.validate_file("models.py", "", code)
        import_errors = [i for i in report.issues if i.category == "import"]
        self.assertGreater(len(import_errors), 0)

    def test_foreignkey_missing_on_delete(self):
        """ForeignKey without on_delete should be caught"""
        code = (
            "from django.db import models\n"
            "class Post(models.Model):\n"
            "    author = models.ForeignKey('User')\n"
        )
        report = self.validator.validate_file("models.py", "", code, file_type="model")
        api_errors = [i for i in report.issues if i.category == "api_compat" and "on_delete" in i.message]
        self.assertGreater(len(api_errors), 0)

    def test_foreignkey_with_on_delete_passes(self):
        """ForeignKey with on_delete should pass"""
        code = (
            "from django.db import models\n"
            "class Post(models.Model):\n"
            "    author = models.ForeignKey('User', on_delete=models.CASCADE)\n"
        )
        report = self.validator.validate_file("models.py", "", code, file_type="model")
        on_delete_errors = [i for i in report.issues if "on_delete" in i.message]
        self.assertEqual(len(on_delete_errors), 0)

    def test_old_url_pattern_detected(self):
        """Old url() with regex should be flagged"""
        code = (
            "from django.urls import re_path\n"
            "urlpatterns = [\n"
            "    url(r'^admin/', admin_site.urls),\n"
            "]\n"
        )
        report = self.validator.validate_file("urls.py", "", code, file_type="urls")
        url_errors = [i for i in report.issues if "url()" in i.message]
        self.assertGreater(len(url_errors), 0)

    def test_removed_settings_detected(self):
        """MIDDLEWARE_CLASSES should be flagged as removed"""
        code = "MIDDLEWARE_CLASSES = ['django.middleware.common.CommonMiddleware']\n"
        report = self.validator.validate_file("settings.py", "", code, file_type="settings")
        setting_errors = [i for i in report.issues if "MIDDLEWARE_CLASSES" in i.message]
        self.assertGreater(len(setting_errors), 0)

    def test_clean_migrated_code_passes(self):
        """Properly migrated code should pass all Tier 1 checks"""
        code = (
            "from django.urls import path, re_path\n"
            "from django.utils.translation import gettext_lazy as _\n"
            "from . import views\n\n"
            "urlpatterns = [\n"
            "    path('admin/', admin.site.urls),\n"
            "    path('api/users/', views.user_list),\n"
            "]\n"
        )
        report = self.validator.validate_file("urls.py", "", code, file_type="urls")
        errors = [i for i in report.issues if i.severity == "error"]
        self.assertEqual(len(errors), 0)
        self.assertTrue(report.passed)


class ValidatorTier2Tests(TestCase):
    """Test Tier 2: Cross-File Consistency"""

    def setUp(self):
        self.validator = ValidatorAgent()

    def test_import_chain_catches_missing_export(self):
        """Importing a name that doesn't exist in the related file should warn"""
        migrated_views = (
            "from .models import Post, OldModelName\n"
            "def view(request):\n"
            "    return Post.objects.all()\n"
        )
        related_models = (
            "from django.db import models\n"
            "class Post(models.Model):\n"
            "    title = models.CharField(max_length=100)\n"
        )
        report = self.validator.validate_file(
            file_path="myapp/views.py",
            original_code="",
            migrated_code=migrated_views,
            file_type="view",
            related_files={"myapp/models.py": related_models},
        )
        cross_file_errors = [i for i in report.issues if i.category == "cross_file"]
        # Should detect OldModelName not in models
        self.assertGreater(len(cross_file_errors), 0)

    def test_serializer_field_mismatch_warned(self):
        """Serializer fields not matching model fields should warn"""
        migrated_serializer = (
            "from rest_framework import serializers\n"
            "from .models import Post\n\n"
            "class PostSerializer(serializers.ModelSerializer):\n"
            "    class Meta:\n"
            "        model = Post\n"
            "        fields = ['id', 'title', 'nonexistent_field']\n"
        )
        related_models = (
            "from django.db import models\n"
            "class Post(models.Model):\n"
            "    title = models.CharField(max_length=100)\n"
            "    body = models.TextField()\n"
        )
        report = self.validator.validate_file(
            file_path="myapp/serializers.py",
            original_code="",
            migrated_code=migrated_serializer,
            file_type="serializer",
            related_files={"myapp/models.py": related_models},
        )
        field_warnings = [i for i in report.issues if "nonexistent_field" in i.message]
        self.assertGreater(len(field_warnings), 0)


class MigrationContextTests(TestCase):
    """Test MigrationContext shared state"""

    def setUp(self):
        self.ctx = MigrationContext(
            repo_id="test123",
            source_version="2.x",
            target_version="5.1",
        )

    def test_add_original_file(self):
        """Adding original file should track it"""
        self.ctx.add_original_file("models.py", "class Foo: pass", "model")
        self.assertEqual(self.ctx.stats["total_files"], 1)
        self.assertIn("models.py", self.ctx.original_files)

    def test_add_migration_result(self):
        """Successful migration should update migrated_files"""
        self.ctx.add_migration_result("views.py", {
            "success": True,
            "migrated_code": "from django.urls import path",
        })
        self.assertIn("views.py", self.ctx.migrated_files)
        self.assertEqual(self.ctx.stats["migrated_count"], 1)

    def test_repair_count_tracking(self):
        """Repair attempts should be tracked per file"""
        self.ctx.add_repair_attempt("views.py", {"success": False, "error": "nope"})
        self.ctx.add_repair_attempt("views.py", {"success": True, "repaired_code": "fixed"})
        self.assertEqual(self.ctx.get_repair_count("views.py"), 2)
        self.assertEqual(self.ctx.stats["total_repair_attempts"], 2)

    def test_related_files_by_app_prefix(self):
        """Related files should include same-app files"""
        self.ctx.migrated_files["myapp/models.py"] = "class M: pass"
        self.ctx.migrated_files["myapp/views.py"] = "def v(): pass"
        self.ctx.migrated_files["other/models.py"] = "class X: pass"

        related = self.ctx.get_related_files("myapp/urls.py")
        self.assertIn("myapp/models.py", related)
        self.assertIn("myapp/views.py", related)
        self.assertNotIn("other/models.py", related)

    def test_context_for_migration(self):
        """get_context_for_migration should return full context dict"""
        self.ctx.add_original_file("views.py", "old code", "view")
        context = self.ctx.get_context_for_migration("views.py")
        self.assertEqual(context["file_path"], "views.py")
        self.assertEqual(context["original_code"], "old code")
        self.assertEqual(context["source_version"], "2.x")
        self.assertEqual(context["target_version"], "5.1")

    def test_summary_serialization(self):
        """Summary should be a clean dict"""
        summary = self.ctx.get_summary()
        self.assertEqual(summary["repo_id"], "test123")
        self.assertIn("stats", summary)
        self.assertIn("files_migrated", summary)


class ValidationReportTests(TestCase):
    """Test ValidationReport logic"""

    def test_report_passes_with_no_errors(self):
        """Report should pass if no error-severity issues"""
        report = ValidationReport("test.py")
        report.add_issue(ValidationIssue(
            tier=1, severity="warning", category="import",
            message="Minor warning", file_path="test.py"
        ))
        self.assertTrue(report.passed)

    def test_report_fails_with_error(self):
        """Report should fail if any error-severity issue added"""
        report = ValidationReport("test.py")
        report.add_issue(ValidationIssue(
            tier=1, severity="error", category="syntax",
            message="Syntax error", file_path="test.py"
        ))
        self.assertFalse(report.passed)
        self.assertFalse(report.tier1_passed)

    def test_report_to_dict(self):
        """to_dict should include all fields"""
        report = ValidationReport("test.py")
        d = report.to_dict()
        self.assertEqual(d["file_path"], "test.py")
        self.assertTrue(d["passed"])
        self.assertEqual(d["total_issues"], 0)
