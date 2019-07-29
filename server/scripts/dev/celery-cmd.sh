#!/bin/sh

export IS_CELERY=true

su -c "celery worker -A apps.core.celery -B -l info -c 2" -s /bin/sh daemon
