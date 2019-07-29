"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `developement`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""
from os import environ
from split_settings.tools import optional, include

ENV = environ.get("DJANGO_ENV") or "development"

base_settings = [
    "components/utils.py",
    "components/vault.py",
    "components/base.py",
    "components/paths.py",
    "components/apps.py",
    "components/middleware.py",
    "components/database.py",
    "components/cache.py",
    "components/email.py",
    "components/rest.py",
    "components/graphql.py",
    "components/templates.py",
    "components/logging.py",
    "components/metrics.py",
    "components/constance.py",
    # Select the right env:
    "environments/%s.py" % ENV,
    # Optionally override some settings:
    optional("environments/local.py"),
]

# Include settings:
include(*base_settings)
