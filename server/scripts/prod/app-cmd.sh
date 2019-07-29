#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate
# Number of workers should be about ~ VCPU * 2 + 1
uwsgi --ini uwsgi.ini:prod
