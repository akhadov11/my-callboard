"""
Email settings.
"""

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = vault_settings.get(
    "DJANGO_DEFAULT_FROM_EMAIL" "noreply@example.com"
)
EMAIL_HOST = vault_settings.get("DJANGO_EMAIL_HOST", "smtp.sendgrid.net")
EMAIL_HOST_USER = vault_settings.get("DJANGO_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = vault_settings.get("DJANGO_EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = int(vault_settings.get("DJANGO_EMAIL_PORT", "587"))
EMAIL_USE_TLS = str2bool(vault_settings.get("DJANGO_EMAIL_USE_TLS", "True"))
