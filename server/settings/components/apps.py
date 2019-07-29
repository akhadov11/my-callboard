"""
Django apps settings.
"""

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    "rest_framework",
    'rest_framework.authtoken',
    "rest_framework_swagger",
    "django_filters",
    "graphene_django",
    "corsheaders",
    "constance",
    'mptt',

    "apps.core.apps.CoreConfig",
    "apps.account.apps.AccountConfig",
    "apps.api.apps.ApiConfig",
    "apps.board.apps.BoardConfig",
    "apps.gallery.apps.GalleryConfig",
]

# Site framework
SITE_ID = 1

# CORS
CORS_ORIGIN_WHITELIST = vault_settings.get(
    "DJANGO_CORS_ORIGIN_WHITELIST", "http://localhost"
).split(",")

# Silk
if SILK_PROFILING:
    INSTALLED_APPS += ("silk",)

SILKY_PYTHON_PROFILER = True
SILKY_PYTHON_PROFILER_BINARY = True
SILKY_META = True

# Constance
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_DATABASE_CACHE_BACKEND = "constance"
