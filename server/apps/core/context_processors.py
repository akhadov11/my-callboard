from django.conf import settings


def core_settings(_):
    return {
        "ENVIRONMENT_NAME": settings.ENVIRONMENT_NAME,
        "ENVIRONMENT_COLOR": settings.ENVIRONMENT_COLOR,
    }
