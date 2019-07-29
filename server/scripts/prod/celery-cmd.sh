#!/bin/sh

export IS_CELERY=true

su -c "celery worker -A apps.core.celery -B -l WARNING -c 4" -s /bin/sh daemon
