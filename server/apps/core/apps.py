from django.apps import AppConfig
from django.conf import settings

from apps.core.services.redis import redis
from apps.core.services.statsd import statsd


class CoreConfig(AppConfig):
    name = "apps.core"

    def ready(self):
        redis.init_app()
        statsd.start(flush_in_thread=not settings.IS_CELERY)
