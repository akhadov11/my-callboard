import pytest

from django.core.exceptions import PermissionDenied

from unittest.mock import Mock

from apps.api.graphql.utils.decorators import is_authenticated, is_staff
from apps.core.tests.utils import raises


@pytest.mark.parametrize(
    "raise_exception, exception, authenticated, expected",
    [
        (True, PermissionDenied, False, "nothing expected"),
        (False, None, False, None),
        (True, None, True, "value"),
        (False, None, True, "value"),
    ],
)
def test_is_authenticated(raise_exception, exception, authenticated, expected):
    class SomeMutation(object):
        @is_authenticated(raise_exception=raise_exception)
        def some_func(self, *_):
            return "value"

    info = Mock(**{"context.user.is_authenticated": authenticated})
    with raises(exception):
        mutation = SomeMutation()
        assert expected == mutation.some_func(info, {})


@pytest.mark.parametrize(
    "raise_exception, exception, is_user_staff, expected",
    [
        (True, PermissionDenied, False, "nothing expected"),
        (False, None, False, None),
        (True, None, True, "value"),
        (False, None, True, "value"),
    ],
)
def test_is_staff(raise_exception, exception, is_user_staff, expected):
    class SomeMutation(object):
        @is_staff(raise_exception=raise_exception)
        def some_func(self, *_):
            return "value"

    info = Mock(**{"context.user.is_staff": is_user_staff})
    with raises(exception):
        mutation = SomeMutation()
        assert expected == mutation.some_func(info, {})
