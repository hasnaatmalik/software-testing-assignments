"""
Minimal Django settings for mutation testing.
Only contains what's needed to run test_validator.py and MigrationContext tests.
"""

SECRET_KEY = 'mutation-testing-secret-key-not-for-production'
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'repositories',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# No URLs needed for these tests
ROOT_URLCONF = 'urls_for_test'
