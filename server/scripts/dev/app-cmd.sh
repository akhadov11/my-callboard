#!/bin/sh

# adding ssh access with user "root" and password "root"
apk add --no-cache openssh screen \
    && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
    && echo "root:root" | chpasswd \
    && ssh-keygen -A

# create privilege separation directory
mkdir -p /var/run/sshd
# run sshd in background
screen -dmS ssh bash -c '/usr/sbin/sshd -D -e'

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
