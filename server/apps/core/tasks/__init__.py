from celery.utils.log import get_task_logger

from apps.core.celery import app, Queues
from apps.core.services.statsd import statsd

task_logger = get_task_logger(__name__)


@app.task(queue=Queues.HEALTH_CHECK, name="core.general.health_check")
def health_check():
    statsd.increment_counter("callboard.core.general.health_check")
