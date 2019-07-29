from functools import wraps

from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

User = get_user_model()


def is_authenticated(raise_exception=False):
    def inner(func):
        @wraps(func)
        def wrapper(obj, info, *args, **kwargs):
            if not info.context.user.is_authenticated:
                if raise_exception:
                    # graphene will catch it and transform to response['errors']
                    raise PermissionDenied

                return

            return func(obj, info, *args, **kwargs)

        return wrapper

    return inner


def is_staff(raise_exception=False):
    def inner(func):
        @wraps(func)
        def wrapper(obj, info, *args, **kwargs):
            if not info.context.user.is_staff:
                if raise_exception:
                    raise PermissionDenied
                return
            return func(obj, info, *args, **kwargs)

        return wrapper

    return inner
