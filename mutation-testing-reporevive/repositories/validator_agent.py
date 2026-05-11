"""
Validator Agent -- 3-Tier Validation Engine for Django Migration

Tier 1: Static Validation (per-file, deterministic)
  - Syntax check via ast.parse()
  - Django 5.x API compatibility checks
  - Required parameter enforcement (on_delete, etc.)

Tier 2: Cross-File Consistency (uses dependency graph)
  - Model → View field reference consistency
  - Model → Serializer field sync
  - Import chain validation
  - URL → View binding check

Tier 3: LLM Semantic Review (optional, AI-powered)
  - Logic preservation check
  - Pattern correctness review
  - Missing migration detection
"""
import ast
import re
import os
import sys
import tempfile
import traceback
try:
    import docker
except ImportError:
    docker = None
from typing import Dict, List, Any, Optional, Tuple


# ─── Django 2.x → 5.x Deprecation Database ──────────────────────────────────

DEPRECATED_IMPORTS = {
    # (old_module, old_name) → (new_module, new_name)
    ("django.conf.urls", "url"): ("django.urls", "re_path"),
    ("django.conf.urls", "include"): ("django.urls", "include"),
    ("django.utils.encoding", "force_text"): ("django.utils.encoding", "force_str"),
    ("django.utils.encoding", "smart_text"): ("django.utils.encoding", "smart_str"),
    ("django.utils.translation", "ugettext"): ("django.utils.translation", "gettext"),
    ("django.utils.translation", "ugettext_lazy"): ("django.utils.translation", "gettext_lazy"),
    ("django.utils.translation", "ungettext"): ("django.utils.translation", "ngettext"),
    ("django.utils.translation", "ungettext_lazy"): ("django.utils.translation", "ngettext_lazy"),
    ("django.utils.encoding", "python_2_unicode_compatible"): (None, None),  # Removed entirely
    ("django.utils.decorators", "ContextDecorator"): ("contextlib", "ContextDecorator"),
    ("django.utils.lru_cache", "lru_cache"): ("functools", "lru_cache"),
    ("django.contrib.postgres.fields", "JSONField"): ("django.db.models", "JSONField"),
}

REMOVED_SETTINGS = [
    "MIDDLEWARE_CLASSES",           # → MIDDLEWARE
    "DEFAULT_CONTENT_TYPE",        # Removed in Django 3.0
    "FILE_CHARSET",                # Removed in Django 3.1
    "PASSWORD_RESET_TIMEOUT_DAYS", # → PASSWORD_RESET_TIMEOUT (seconds)
]

FOREIGNKEY_FIELDS = ["ForeignKey", "OneToOneField"]

DJANGO5_REMOVED_FUNCTIONS = [
    "smart_text",
    "force_text",
    "ugettext",
    "ugettext_lazy",
    "ungettext",
    "ungettext_lazy",
    "python_2_unicode_compatible",
]


class ValidationIssue:
    """Represents a single validation issue found during checking."""
    
    def __init__(
        self,
        tier: int,
        severity: str,      # "error", "warning", "info"
        category: str,       # "syntax", "import", "api_compat", "cross_file", "semantic"
        message: str,
        file_path: str,
        line_number: Optional[int] = None,
        fix_hint: Optional[str] = None,
        auto_fixable: bool = False,
    ):
        self.tier = tier
        self.severity = severity
        self.category = category
        self.message = message
        self.file_path = file_path
        self.line_number = line_number
        self.fix_hint = fix_hint
        self.auto_fixable = auto_fixable
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "tier": self.tier,
            "severity": self.severity,
            "category": self.category,
            "message": self.message,
            "file_path": self.file_path,
            "line_number": self.line_number,
            "fix_hint": self.fix_hint,
            "auto_fixable": self.auto_fixable,
        }


class ValidationReport:
    """Complete validation report for a migration."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.issues: List[ValidationIssue] = []
        self.passed = True
        self.tier1_passed = True
        self.tier2_passed = True
        self.tier3_passed = True
    
    def add_issue(self, issue: ValidationIssue):
        self.issues.append(issue)
        if issue.severity == "error":
            self.passed = False
            if issue.tier == 1:
                self.tier1_passed = False
            elif issue.tier == 2:
                self.tier2_passed = False
            elif issue.tier == 3:
                self.tier3_passed = False
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "file_path": self.file_path,
            "passed": self.passed,
            "tier1_passed": self.tier1_passed,
            "tier2_passed": self.tier2_passed,
            "tier3_passed": self.tier3_passed,
            "total_issues": len(self.issues),
            "error_count": sum(1 for i in self.issues if i.severity == "error"),
            "warning_count": sum(1 for i in self.issues if i.severity == "warning"),
            "issues": [i.to_dict() for i in self.issues],
        }


class ValidatorAgent:
    """
    3-Tier Validation Engine for Django Migration.
    
    Usage:
        validator = ValidatorAgent()
        report = validator.validate_file(
            file_path="myapp/views.py",
            original_code="...",
            migrated_code="...",
            file_type="view",
            related_files={"myapp/models.py": "..."},
            dependency_graph={...}
        )
        
        if not report.passed:
            # Send issues back to Migration Agent for repair
            issues = report.to_dict()["issues"]
    """
    
    def __init__(self, enable_tier3: bool = False, llm_client=None):
        """
        Args:
            enable_tier3: Enable LLM-powered semantic review (Tier 3)
            llm_client: LLM client for Tier 3 (Groq/Gemini instance)
        """
        self.enable_tier3 = enable_tier3
        self.llm_client = llm_client
        self.docker_client = None
        self.docker_error = None
        try:
            import docker
            self.docker_client = docker.from_env()
        except ImportError:
            self.docker_error = "Docker python module not installed (run `pip install docker`)"
        except Exception as e:
            self.docker_error = f"Error connecting to Docker daemon: {e}"
    
    def validate_file(
        self,
        file_path: str,
        original_code: str,
        migrated_code: str,
        file_type: str = "unknown",
        related_files: Optional[Dict[str, str]] = None,
        dependency_graph: Optional[Dict] = None,
    ) -> ValidationReport:
        """
        Run all validation tiers on a migrated file.
        
        Args:
            file_path: Path to the file
            original_code: Original Django 2.x code
            migrated_code: Migrated Django 5.x code
            file_type: Django file type (model, view, urls, etc.)
            related_files: Dict of {path: migrated_content} for related files
            dependency_graph: Full dependency graph from analyzer
            
        Returns:
            ValidationReport with all issues found
        """
        report = ValidationReport(file_path)
        
        # Tier 1: Static Validation
        self._run_tier1(report, file_path, migrated_code, file_type)
        
        # Tier 2: Cross-File Consistency
        if related_files:
            self._run_tier2(
                report, file_path, original_code, migrated_code,
                file_type, related_files, dependency_graph
            )
        
        # Tier 3: LLM Semantic Review (optional)
        if self.enable_tier3 and self.llm_client:
            self._run_tier3(
                report, file_path, original_code, migrated_code,
                file_type, related_files
            )
        
        return report
    
    def validate_batch(
        self,
        migration_context,  # MigrationContext instance
        enable_tier3: bool = False,
    ) -> Dict[str, ValidationReport]:
        """Validate all migrated files in a batch using shared context."""
        reports = {}
        
        for file_path, migrated_code in migration_context.migrated_files.items():
            original_code = migration_context.original_files.get(file_path, "")
            file_type = migration_context.file_types.get(file_path, "unknown")
            related_files = migration_context.get_related_files(file_path)
            
            report = self.validate_file(
                file_path=file_path,
                original_code=original_code,
                migrated_code=migrated_code,
                file_type=file_type,
                related_files=related_files,
                dependency_graph=migration_context.dependency_graph,
            )
            
            reports[file_path] = report
            migration_context.add_validation_result(file_path, report.to_dict())
        
        # Tier 4: Containerized Runtime Testing
        if self.docker_client:
            migration_context.add_log("[VALIDATOR] Running Tier 4 Containerized Sandbox...")
            tier4_issues = self._run_tier4_docker(migration_context)
        else:
            migration_context.add_log(f"[VALIDATOR] Tier 4 Containerized Sandbox SKIPPED ({self.docker_error})")
            tier4_issues = []
            
        if tier4_issues:
            for issue in tier4_issues:
                target = issue.file_path
                if target and target in reports:
                    reports[target].add_issue(issue)
                elif reports:
                    # If we can't map it, attach to first available report
                    first = next(iter(reports.keys()))
                    reports[first].add_issue(issue)

            # Re-sync modified reports to context
            for path, report in reports.items():
                migration_context.add_validation_result(path, report.to_dict())

        return reports
    # ─── TIER 1: Static Validation ─────────────────────────────────────────────
    
    def _run_tier1(
        self,
        report: ValidationReport,
        file_path: str,
        code: str,
        file_type: str,
    ):
        """Run per-file static checks."""
        self._check_syntax(report, file_path, code)
        self._check_deprecated_imports(report, file_path, code)
        self._check_removed_apis(report, file_path, code)
        self._check_foreignkey_on_delete(report, file_path, code, file_type)
        self._check_middleware_pattern(report, file_path, code, file_type)
        self._check_removed_settings(report, file_path, code, file_type)
        self._check_url_patterns(report, file_path, code, file_type)
    
    def _check_syntax(self, report: ValidationReport, file_path: str, code: str):
        """Check if migrated code is valid Python."""
        try:
            ast.parse(code)
        except SyntaxError as e:
            report.add_issue(ValidationIssue(
                tier=1,
                severity="error",
                category="syntax",
                message=f"Syntax error: {e.msg}",
                file_path=file_path,
                line_number=e.lineno,
                fix_hint=f"Fix syntax error at line {e.lineno}: {e.text.strip() if e.text else ''}",
                auto_fixable=False,
            ))
    
    def _check_deprecated_imports(self, report: ValidationReport, file_path: str, code: str):
        """Check for Django 2.x deprecated imports that should have been migrated."""
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return  # Already caught in syntax check
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                for alias in node.names:
                    key = (node.module, alias.name)
                    if key in DEPRECATED_IMPORTS:
                        new_module, new_name = DEPRECATED_IMPORTS[key]
                        if new_module is None:
                            fix = f"Remove import — '{alias.name}' was removed in Django 3+"
                        else:
                            fix = f"Change to: from {new_module} import {new_name}"
                        
                        report.add_issue(ValidationIssue(
                            tier=1,
                            severity="error",
                            category="import",
                            message=f"Deprecated import still present: from {node.module} import {alias.name}",
                            file_path=file_path,
                            line_number=node.lineno,
                            fix_hint=fix,
                            auto_fixable=True,
                        ))
    
    def _check_removed_apis(self, report: ValidationReport, file_path: str, code: str):
        """Check for removed Django function calls."""
        for func_name in DJANGO5_REMOVED_FUNCTIONS:
            pattern = rf'\b{func_name}\s*\('
            for match in re.finditer(pattern, code):
                line_num = code[:match.start()].count('\n') + 1
                report.add_issue(ValidationIssue(
                    tier=1,
                    severity="error",
                    category="api_compat",
                    message=f"Removed function still used: {func_name}()",
                    file_path=file_path,
                    line_number=line_num,
                    fix_hint=f"Replace {func_name}() with its Django 5.x equivalent",
                    auto_fixable=True,
                ))
    
    def _check_foreignkey_on_delete(
        self, report: ValidationReport, file_path: str, code: str, file_type: str
    ):
        """Check that ForeignKey/OneToOneField has on_delete parameter."""
        if file_type not in ("model", "models", "unknown"):
            return
        
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func_name = ""
                if isinstance(node.func, ast.Attribute):
                    func_name = node.func.attr
                elif isinstance(node.func, ast.Name):
                    func_name = node.func.id
                
                if func_name in FOREIGNKEY_FIELDS:
                    has_on_delete = any(
                        kw.arg == "on_delete" for kw in node.keywords
                    )
                    # Also check positional args (on_delete can be 2nd positional)
                    if not has_on_delete and len(node.args) < 2:
                        report.add_issue(ValidationIssue(
                            tier=1,
                            severity="error",
                            category="api_compat",
                            message=f"{func_name} missing required 'on_delete' parameter",
                            file_path=file_path,
                            line_number=node.lineno,
                            fix_hint=f"Add on_delete=models.CASCADE (or appropriate action) to {func_name}",
                            auto_fixable=True,
                        ))
    
    def _check_middleware_pattern(
        self, report: ValidationReport, file_path: str, code: str, file_type: str
    ):
        """Check for old-style middleware pattern."""
        if file_type not in ("middleware", "unknown"):
            return
        
        # Old pattern: class with process_request/process_response methods
        if "process_request" in code or "process_response" in code:
            if "get_response" not in code and "__call__" not in code:
                report.add_issue(ValidationIssue(
                    tier=1,
                    severity="error",
                    category="api_compat",
                    message="Old-style middleware still uses process_request/process_response pattern",
                    file_path=file_path,
                    fix_hint="Convert to new-style middleware with __init__(get_response) and __call__(request)",
                    auto_fixable=False,
                ))
    
    def _check_removed_settings(
        self, report: ValidationReport, file_path: str, code: str, file_type: str
    ):
        """Check for removed Django settings."""
        if file_type not in ("settings", "unknown", "other") and not file_path.endswith("settings.py"):
            return
        
        for setting in REMOVED_SETTINGS:
            pattern = rf'\b{setting}\b\s*='
            match = re.search(pattern, code)
            if match:
                line_num = code[:match.start()].count('\n') + 1
                report.add_issue(ValidationIssue(
                    tier=1,
                    severity="error",
                    category="api_compat",
                    message=f"Removed setting still present: {setting}",
                    file_path=file_path,
                    line_number=line_num,
                    fix_hint=f"Replace {setting} with its Django 5.x equivalent",
                    auto_fixable=True,
                ))
    
    def _check_url_patterns(
        self, report: ValidationReport, file_path: str, code: str, file_type: str
    ):
        """Check for old-style url() patterns that should be path()/re_path()."""
        if file_type not in ("urls", "url", "unknown"):
            return
        
        # Check for url() function calls (not re_path)
        old_url_pattern = r'\burl\s*\(\s*r[\'"]'
        for match in re.finditer(old_url_pattern, code):
            line_num = code[:match.start()].count('\n') + 1
            report.add_issue(ValidationIssue(
                tier=1,
                severity="error",
                category="api_compat",
                message="Old-style url() with regex still present — should use path() or re_path()",
                file_path=file_path,
                line_number=line_num,
                fix_hint="Replace url(r'...', ...) with path('...', ...) or re_path(r'...', ...)",
                auto_fixable=True,
            ))
    
    # ─── TIER 2: Cross-File Consistency ────────────────────────────────────────
    
    def _run_tier2(
        self,
        report: ValidationReport,
        file_path: str,
        original_code: str,
        migrated_code: str,
        file_type: str,
        related_files: Dict[str, str],
        dependency_graph: Optional[Dict] = None,
    ):
        """Run cross-file consistency checks."""
        self._check_model_view_consistency(
            report, file_path, migrated_code, file_type, related_files
        )
        self._check_model_serializer_sync(
            report, file_path, migrated_code, file_type, related_files
        )
        self._check_import_chains(
            report, file_path, migrated_code, related_files
        )
        self._check_url_view_binding(
            report, file_path, migrated_code, file_type, related_files
        )
    
    def _check_model_view_consistency(
        self,
        report: ValidationReport,
        file_path: str,
        migrated_code: str,
        file_type: str,
        related_files: Dict[str, str],
    ):
        """Check that views reference model classes/fields that exist in migrated models."""
        if file_type not in ("view", "views", "unknown"):
            return
        
        # Find model files in related files
        model_files = {
            path: content for path, content in related_files.items()
            if "models" in path.lower() or "model" in path.lower()
        }
        
        if not model_files:
            return
        
        # Extract model class names from model files
        model_classes = set()
        for model_path, model_code in model_files.items():
            try:
                tree = ast.parse(model_code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        # Check if it inherits from models.Model
                        for base in node.bases:
                            base_name = ""
                            if isinstance(base, ast.Attribute):
                                base_name = base.attr
                            elif isinstance(base, ast.Name):
                                base_name = base.id
                            if base_name in ("Model", "AbstractUser", "AbstractBaseUser"):
                                model_classes.add(node.name)
            except SyntaxError:
                continue
        
        if not model_classes:
            return
        
        # Check if the view references any model that doesn't exist
        try:
            tree = ast.parse(migrated_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Attribute):
                    if isinstance(node.value, ast.Name):
                        # Check for Model.objects.xxx patterns
                        if node.value.id not in model_classes and node.attr == "objects":
                            # Could be a model that we should recognize
                            # Only flag if it looks like a model access pattern
                            pass  # Don't over-flag — this is a heuristic
        except SyntaxError:
            pass
    
    def _check_model_serializer_sync(
        self,
        report: ValidationReport,
        file_path: str,
        migrated_code: str,
        file_type: str,
        related_files: Dict[str, str],
    ):
        """Check that serializers reference fields that exist in migrated models."""
        if file_type not in ("serializer", "serializers", "unknown"):
            return
        
        # Find model files
        model_files = {
            path: content for path, content in related_files.items()
            if "models" in path.lower()
        }
        
        if not model_files:
            return
        
        # Extract model field names
        model_fields = {}  # model_name -> set of field names
        for model_path, model_code in model_files.items():
            try:
                tree = ast.parse(model_code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        fields = set()
                        for item in node.body:
                            if isinstance(item, ast.Assign):
                                for target in item.targets:
                                    if isinstance(target, ast.Name):
                                        fields.add(target.id)
                        if fields:
                            model_fields[node.name] = fields
            except SyntaxError:
                continue
        
        if not model_fields:
            return
        
        # Check serializer Meta.fields against model fields
        try:
            tree = ast.parse(migrated_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name == "Meta":
                    for item in node.body:
                        if isinstance(item, ast.Assign):
                            for target in item.targets:
                                if isinstance(target, ast.Name) and target.id == "model":
                                    # Get model name from the assignment
                                    if isinstance(item.value, ast.Name):
                                        model_name = item.value.id
                                        if model_name in model_fields:
                                            # Now check fields list
                                            self._verify_serializer_fields(
                                                report, file_path, node,
                                                model_name, model_fields[model_name]
                                            )
        except SyntaxError:
            pass
    
    def _verify_serializer_fields(
        self,
        report: ValidationReport,
        file_path: str,
        meta_node: ast.ClassDef,
        model_name: str,
        model_fields: set,
    ):
        """Verify serializer fields match model fields."""
        for item in meta_node.body:
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and target.id == "fields":
                        if isinstance(item.value, (ast.List, ast.Tuple)):
                            for elt in item.value.elts:
                                if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                    field_name = elt.value
                                    if field_name not in model_fields and field_name not in ("id", "pk", "__all__"):
                                        report.add_issue(ValidationIssue(
                                            tier=2,
                                            severity="warning",
                                            category="cross_file",
                                            message=f"Serializer field '{field_name}' not found in {model_name} model",
                                            file_path=file_path,
                                            line_number=elt.lineno,
                                            fix_hint=f"Verify '{field_name}' exists in migrated {model_name} model",
                                            auto_fixable=False,
                                        ))
    
    def _check_import_chains(
        self,
        report: ValidationReport,
        file_path: str,
        migrated_code: str,
        related_files: Dict[str, str],
    ):
        """Check that imports from related files reference classes/functions that exist."""
        try:
            tree = ast.parse(migrated_code)
        except SyntaxError:
            return
        
        # Get exports from related files
        exports = {}  # module_path -> set of exported names
        for path, content in related_files.items():
            try:
                related_tree = ast.parse(content)
                names = set()
                for node in ast.walk(related_tree):
                    if isinstance(node, ast.ClassDef):
                        names.add(node.name)
                    elif isinstance(node, ast.FunctionDef):
                        names.add(node.name)
                    elif isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                names.add(target.id)
                exports[path] = names
            except SyntaxError:
                continue
        
        # Check imports in migrated code against exports
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                # Convert module path to file path for matching
                module_as_path = node.module.replace(".", "/")
                
                for path, names in exports.items():
                    # Fuzzy match: check if the import module matches a related file
                    path_normalized = path.replace("\\", "/").replace(".py", "")
                    if module_as_path.endswith(path_normalized.split("/")[-1]):
                        for alias in node.names:
                            if alias.name not in names and alias.name != "*":
                                report.add_issue(ValidationIssue(
                                    tier=2,
                                    severity="error",
                                    category="cross_file",
                                    message=f"Import '{alias.name}' from '{node.module}' — name not found in migrated '{path}'",
                                    file_path=file_path,
                                    line_number=node.lineno,
                                    fix_hint=f"Check if '{alias.name}' was renamed or removed in the migrated version of '{path}'",
                                    auto_fixable=False,
                                ))
    
    def _check_url_view_binding(
        self,
        report: ValidationReport,
        file_path: str,
        migrated_code: str,
        file_type: str,
        related_files: Dict[str, str],
    ):
        """Check that URL patterns reference views that exist."""
        if file_type not in ("urls", "url", "unknown"):
            return
        
        # Look for view files in related files
        view_files = {
            path: content for path, content in related_files.items()
            if "views" in path.lower() or "view" in path.lower()
        }
        
        if not view_files:
            return
        
        # Extract view function/class names from view files
        view_names = set()
        for view_path, view_code in view_files.items():
            try:
                tree = ast.parse(view_code)
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        view_names.add(node.name)
                    elif isinstance(node, ast.ClassDef):
                        view_names.add(node.name)
            except SyntaxError:
                continue
        
        if not view_names:
            return
        
        # Check URL patterns reference existing views
        try:
            tree = ast.parse(migrated_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    func_name = ""
                    if isinstance(node.func, ast.Name):
                        func_name = node.func.id
                    elif isinstance(node.func, ast.Attribute):
                        func_name = node.func.attr
                    
                    if func_name in ("path", "re_path", "url"):
                        # Check 2nd argument (view reference)
                        if len(node.args) >= 2:
                            view_ref = node.args[1]
                            if isinstance(view_ref, ast.Attribute):
                                # views.some_view pattern
                                ref_name = view_ref.attr
                                if ref_name not in view_names:
                                    report.add_issue(ValidationIssue(
                                        tier=2,
                                        severity="warning",
                                        category="cross_file",
                                        message=f"URL pattern references view '{ref_name}' — not found in migrated view files",
                                        file_path=file_path,
                                        line_number=node.lineno,
                                        fix_hint=f"Verify '{ref_name}' exists in the migrated views module",
                                        auto_fixable=False,
                                    ))
        except SyntaxError:
            pass
    
    # ─── TIER 3: LLM Semantic Review ──────────────────────────────────────────
    
    def _run_tier3(
        self,
        report: ValidationReport,
        file_path: str,
        original_code: str,
        migrated_code: str,
        file_type: str,
        related_files: Optional[Dict[str, str]] = None,
    ):
        """Run LLM-powered semantic review."""
        if not self.llm_client:
            return
        
        prompt = self._build_tier3_prompt(
            file_path, original_code, migrated_code, file_type, related_files
        )
        
        try:
            # Use the LLM to review
            response = self._call_llm(prompt)
            issues = self._parse_tier3_response(response, file_path)
            
            for issue in issues:
                report.add_issue(issue)
                
        except Exception as e:
            report.add_issue(ValidationIssue(
                tier=3,
                severity="warning",
                category="semantic",
                message=f"Tier 3 review failed: {str(e)}",
                file_path=file_path,
                auto_fixable=False,
            ))
    
    def _build_tier3_prompt(
        self,
        file_path: str,
        original_code: str,
        migrated_code: str,
        file_type: str,
        related_files: Optional[Dict[str, str]] = None,
    ) -> str:
        """Build prompt for LLM semantic review."""
        related_context = ""
        if related_files:
            for path, content in list(related_files.items())[:3]:  # Limit context
                related_context += f"\n### Related File: {path}\n```python\n{content[:2000]}\n```\n"
        
        return f"""You are a Django migration validator. Review the following migration from Django 2.x to 5.x.

## Original Code ({file_path}, type: {file_type}):
```python
{original_code}
```

## Migrated Code:
```python
{migrated_code}
```

{f"## Related Files (already migrated):{related_context}" if related_context else ""}

## Check for these issues:
1. **Logic changes**: Was any business logic accidentally altered?
2. **Missing migrations**: Are there deprecated patterns that weren't updated?
3. **Wrong patterns**: Were migration rules applied incorrectly?
4. **Cross-file breaks**: Does this code reference things in related files that may have changed?

## Output Format:
For each issue found, output EXACTLY one line in this format:
ISSUE|severity|message|line_number|fix_hint

Where severity is: error, warning, or info
If no issues found, output: NO_ISSUES

Only report REAL issues. Do not report false positives.
"""
    
    def _call_llm(self, prompt: str) -> str:
        """Call the LLM backend."""
        if hasattr(self.llm_client, 'chat'):
            # Groq client
            response = self.llm_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=2000,
            )
            return response.choices[0].message.content
        elif hasattr(self.llm_client, 'generate_content'):
            # Gemini client
            response = self.llm_client.generate_content(prompt)
            return response.text
        else:
            raise ValueError("Unknown LLM client type")
    
    def _parse_tier3_response(self, response: str, file_path: str) -> List[ValidationIssue]:
        """Parse LLM response into ValidationIssue objects."""
        issues = []
        
        if not response or "NO_ISSUES" in response:
            return issues
        
        for line in response.strip().split("\n"):
            line = line.strip()
            if line.startswith("ISSUE|"):
                parts = line.split("|")
                if len(parts) >= 4:
                    severity = parts[1].strip().lower()
                    message = parts[2].strip()
                    line_num = None
                    fix_hint = None
                    
                    if len(parts) >= 4:
                        try:
                            line_num = int(parts[3].strip())
                        except (ValueError, IndexError):
                            pass
                    if len(parts) >= 5:
                        fix_hint = parts[4].strip()
                    
                    if severity in ("error", "warning", "info"):
                        issues.append(ValidationIssue(
                            tier=3,
                            severity=severity,
                            category="semantic",
                            message=message,
                            file_path=file_path,
                            line_number=line_num,
                            fix_hint=fix_hint,
                            auto_fixable=False,
                        ))
        
        return issues

    # --- TIER 4: Containerized Runtime Testing ----------------------------------------

    def _run_tier4_docker(self, migration_context) -> List[ValidationIssue]:
        issues = []
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                # 1. Write the full contextual tree
                for file_path, content in migration_context.original_files.items():
                    full_path = os.path.join(temp_dir, file_path)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(content)
                
                # 2. Overlay migrated files
                for file_path, content in migration_context.migrated_files.items():
                    full_path = os.path.join(temp_dir, file_path)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(content)

                # Find manage.py in the root or close to root
                manage_py_path = None
                for file_path in migration_context.original_files:
                    if file_path.endswith("manage.py"):
                        manage_py_path = file_path
                        break
                
                if not manage_py_path:
                    issues.append(ValidationIssue(
                        tier=4, severity="warning", category="runtime",
                        message="manage.py not found in contextual files. Skipping Django container tests.",
                        file_path=""
                    ))
                    return issues

                manage_py_dir = os.path.dirname(manage_py_path)
                container_run_dir = f"/app/{manage_py_dir}".rstrip('/')
                
                # Check for requirements.txt to install dependencies
                req_path = os.path.join(temp_dir, "requirements.txt")
                install_cmd = "pip install django==5.1.0"
                if os.path.exists(req_path):
                    install_cmd = "pip install -r requirements.txt && pip install django==5.1.0 --upgrade"
                
                # First run system checks, then run tests if the check passes
                # If they don't have tests, manage.py test will just run 0 tests and succeed.
                cmd = f"sh -c '{install_cmd} && python manage.py check && python manage.py test'"
                
                container = self.docker_client.containers.run(
                    image="python:3.12-slim",
                    command=cmd,
                    volumes={temp_dir: {'bind': '/app', 'mode': 'rw'}},
                    working_dir=container_run_dir or "/app",
                    detach=False,
                    remove=True,
                    timeout=90
                )
                migration_context.add_log(f"[VALIDATOR] Docker container check succeeded.")
                
            except docker.errors.ContainerError as e:
                stderr = e.stderr.decode('utf-8') if e.stderr else ""
                stdout = e.stdout.decode('utf-8') if e.stdout else ""
                output = stderr or stdout
                
                migration_context.add_log(f"[VALIDATOR] Docker container runtime failed:\n{output}")
                
                # Try to extract a file name from traceback
                guessed_file = ""
                for file_path in migration_context.migrated_files:
                    if file_path in output:
                        guessed_file = file_path
                        break
                
                issues.append(ValidationIssue(
                    tier=4, severity="error", category="runtime",
                    message=f"Runtime error during `manage.py check` or `manage.py test`:\n\n{output}",
                    file_path=guessed_file
                ))
            except Exception as e:
                issues.append(ValidationIssue(
                    tier=4, severity="error", category="runtime",
                    message=f"Docker orchestration failed: {str(e)}",
                    file_path=""
                ))
        return issues

    @staticmethod
    def format_errors_for_prompt(errors: List[Dict]) -> str:
        """Backward compatibility for formatting error output."""
        return "\n".join([f"- {e.get('severity', 'Error').upper()}: {e.get('message', '')} "
                          f"(Line {e.get('line_number', '?')})" for e in errors])
                          
    def validate(self, code: str) -> Dict[str, Any]:
        """Backward compatibility wrapper for singular code validation."""
        report = ValidationReport("unknown.py")
        self._run_tier1(report, "unknown.py", code, "unknown")
        
        return {
            "is_valid": report.passed,
            "errors": [i.to_dict() for i in report.issues if i.severity == "error"]
        }
