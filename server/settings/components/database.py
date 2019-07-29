"""
Databases settings.
"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": vault_settings.get("DATABASE_NAME", "callboard"),
        "USER": vault_settings.get("DATABASE_USER", "callboard_user"),
        "PASSWORD": vault_settings.get("DATABASE_PASSWORD", "callboard_secret"),
        "HOST": vault_settings.get("DATABASE_HOST", "postgres"),
        "PORT": vault_settings.get("DATABASE_PORT", "5432"),
        "ATOMIC_REQUESTS": True,
    }
}

DATABASE_ROUTERS = []
