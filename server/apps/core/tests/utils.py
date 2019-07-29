import pytest

from contextlib import contextmanager


def raises(expected_exception, *args, **kwargs):
    """Raises context manager that supports None."""
    if expected_exception:
        return pytest.raises(expected_exception, *args, **kwargs)
    else:

        @contextmanager
        def not_raises():
            try:
                yield
            except Exception as exc:
                raise exc

        return not_raises()
