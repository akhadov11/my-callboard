from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger

from apps.core.services.statsd import statsd

task_logger = get_task_logger(__name__)


def on_success(self, retval, task_id, args, kwargs):
    task_logger.debug("Task %s success" % task_id)


def on_failure(self, exc, task_id, args, kwargs, einfo=None):
    task_logger.debug("Task %s failure" % task_id)
    if isinstance(exc, SoftTimeLimitExceeded):
        task_logger.exception("Task soft time limit exceeded.")


def after_return(self, status, retval, task_id, args, kwargs, einfo=None):
    task_logger.debug("Task %s return" % task_id)
    statsd.flush()


def on_retry(self, exc, task_id, args, kwargs, einfo=None):
    task_logger.debug("Task %s retry" % task_id)
