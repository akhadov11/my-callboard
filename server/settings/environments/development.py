"""
Development environment settings.
"""

ENVIRONMENT_NAME = "Development"
ENVIRONMENT_COLOR = "green"

DEBUG = True

ADMIN_PANEL_AVAILABLE = True

SHOW_GRAPHIQL = True

SILK_PROFILING = True
INSTALLED_APPS += ("silk",)
MIDDLEWARE = ["silk.middleware.SilkyMiddleware"] + MIDDLEWARE

SHOW_API_DOCS = True

SERVE_STATIC_IN_APP = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS += ["django_extensions"]
