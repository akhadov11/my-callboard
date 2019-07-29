"""
Django rest framework, JWT, swagger settings.
"""
import datetime

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": ("rest_framework.pagination.PageNumberPagination"),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "PAGE_SIZE": 50,
    "COERCE_DECIMAL_TO_STRING": True,
}

JWT_AUTH = {
    "JWT_EXPIRATION_DELTA": datetime.timedelta(days=1),
    "JWT_ALLOW_REFRESH": True,
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
}

LOGIN_URL = "rest_framework:login"
LOGOUT_URL = "rest_framework:logout"

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "basic": {"type": "basic"},
        "api_key": {"type": "apiKey", "in": "header", "name": "Authorization"},
    },
    "USE_SESSION_AUTH": True,
    "JSON_EDITOR": True,
    "SHOW_REQUEST_HEADERS": True,
}
