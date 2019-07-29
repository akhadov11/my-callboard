import os

from datetime import timedelta

from django.apps import apps
from django.conf import settings

from celery import Celery
from kombu import Queue

from .celery_handlers import (
    after_return,
    on_success,
    on_retry,
    on_failure,
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


class Queues(object):
    HEALTH_CHECK = "health-check"


app = Celery("callboard-celery")

# Celery settings
# update to "msgpack" after the issus https://github.com/celery/kombu/issues/1037 will be resolved
app.conf.accept_content = ["json"]
app.conf.result_serializer = "json"
app.conf.task_serializer = "json"
app.conf.broker_url = settings.VAULT_SETTINGS.get(
    "CELERY_BROKER_URL", "redis://redis:6379/13"
)
app.conf.result_backend = settings.VAULT_SETTINGS.get(
    "CELERY_RESULT_BACKEND", "redis://redis:6379/14"
)
app.conf.redbeat_redis_url = redbeat_redis_url = settings.VAULT_SETTINGS.get(
    "REDBEAT_REDIS_URL", "redis://redis:6379/15"
)
app.conf.redbeat_lock_key = None
app.conf.task_annotations = {"*": {
    # better not to override "after_return" or just flush metrics for statsd
    # synchronously in the overridden function since ThreadStats is used
    "after_return": after_return,
    "on_success": on_success,
    "on_retry": on_retry,
    "on_failure": on_failure,
}}
app.conf.task_default_queue = "default"
app.conf.task_queues = (
    Queue(Queues.HEALTH_CHECK),
)
app.conf.task_default_exchange = "celery"
app.conf.task_default_exchange_type = "direct"
app.conf.task_soft_time_limit = 300
app.conf.task_time_limit = 360
app.conf.beat_scheduler = "redbeat.RedBeatScheduler"
app.conf.beat_schedule = {
    "core.general.health_check": {
        "task": "core.general.health_check",
        "schedule": timedelta(seconds=10),
    },
}

# Autodiscover tasks
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
