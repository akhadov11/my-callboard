"""
Cache settings.
"""

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = int(
    vault_settings.get("DJANGO_CACHE_MIDDLEWARE_SECONDS", "10")
)
CACHE_MIDDLEWARE_KEY_PREFIX = "django"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": vault_settings.get("DJANGO_CACHE_LOCATION", "redis://redis:6379/0"),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    },
    "sessions": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": vault_settings.get(
            "DJANGO_CACHE_SESSIONS_LOCATION", "redis://redis:6379/1"
        ),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    },
    "constance": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": vault_settings.get(
            "DJANGO_CACHE_CONSTANCE_LOCATION", "redis://redis:6379/2"
        ),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    },
}

REDIS_SOCKET_TIMEOUT = 2
REDIS_SOCKET_CONNECT_TIMEOUT = 2

REDIS_CONNECTION_QUEUE_BASE = vault_settings.get(
    "REDIS_QUEUE_BASE", "redis://redis:6379/3"
)
