"""
Logging settings.
"""
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration

SENTRY_DSN = vault_settings.get("SENTRY_DSN", "")
LOGSTASH_HOST = vault_settings.get("LOGSTASH_HOST", "logstash")
LOGSTASH_PORT = int(vault_settings.get("LOGSTASH_PORT", "5959"))

if IS_CELERY:
    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[CeleryIntegration()], environment=ENV)
else:
    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()], environment=ENV)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d "
                      "%(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "logstash": {
            "level": "INFO",
            "class": "logstash.TCPLogstashHandler",
            "host": LOGSTASH_HOST,
            "port": LOGSTASH_PORT,
            "version": 1,
            "message_type": "django",
            "fqdn": False,
            "tags": ["callboard.%s" % ENV]
        },
    },
    "loggers": {
        "django": {"handlers": ["console", "logstash"], "propagate": True},
        "django.request": {
            "handlers": ["console", "logstash"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["console", "logstash"],
            "level": "INFO",
            "propagate": False,
        },
        "django.template": {
            "handlers": ["console", "logstash"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console", "logstash"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.security.*": {
            "handlers": ["console", "logstash"],
            "level": "WARNING",
            "propagate": False,
        },
        "apps.*": {
            "handlers": ["console", "logstash"],
            "level": "DEBUG" if DEBUG else "INFO",
            "propagate": False,
        },
    },
}
