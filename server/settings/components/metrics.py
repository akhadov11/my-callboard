import datadog

datadog.initialize(
    api_key=vault_settings.get("DATADOG_API_KEY", ""),
    app_key=vault_settings.get("DATADOG_APP_KEY", ""),
)
