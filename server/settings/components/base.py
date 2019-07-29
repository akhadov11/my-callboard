"""
Base variables.
"""
import os

from sys import platform

# flake8: F821
from django.utils.translation import ugettext_lazy as _

# ==============================================================================
# Base variables
# ==============================================================================

ENV = os.getenv("DJANGO_ENV")

IS_LINUX = platform.startswith("linux")

SECRET_KEY = vault_settings.get("DJANGO_SECRET_KEY", "SOME_VERY_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = vault_settings.get("DJANGO_ALLOWED_HOSTS", "*").split(",")

ADMIN_PANEL_AVAILABLE = str2bool(
    vault_settings.get("DJANGO_ADMIN_PANEL_AVAILABLE", "False")
)

SHOW_API_DOCS = str2bool(vault_settings.get("DJANGO_SHOW_API_DOCS", "False"))

SHOW_GRAPHIQL = str2bool(vault_settings.get("DJANGO_SHOW_GRAPHIQL", "False"))

SILK_PROFILING = str2bool(os.getenv("SILK_PROFILING", "0"))

AUTH_USER_MODEL = "account.User"

SERVE_STATIC_IN_APP = False

INTERNAL_IPS = vault_settings.get("DJANGO_INTERNAL_IPS", "127.0.0.1").split(",")

IS_CELERY = str2bool(os.getenv("IS_CELERY", "False"))

ADMINS = []

PREPEND_WWW = False

USE_ETAGS = True

ENVIRONMENT_NAME = "Unknown, environment was not set"
ENVIRONMENT_COLOR = "black"

# ==============================================================================
# Internationalization & Timezone
# ==============================================================================

LANGUAGE_CODE = "en"

LANGUAGE_COOKIE_NAME = "app-language"

LANGUAGES = [("en", _("English"))]

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ==============================================================================
# Authentication & Sessions
# ==============================================================================

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        ".UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "sessions"
