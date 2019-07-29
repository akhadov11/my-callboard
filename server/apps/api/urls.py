from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from apps.api.routers import router
from apps.api.views import Ping

app_name = "api"

urlpatterns = [
    path("ping", Ping.as_view(), name="ping"),
    path("auth/login", obtain_jwt_token, name="auth-token"),
    path("auth/refresh-token", refresh_jwt_token, name="refresh-token"),
    path("auth/verify-token", verify_jwt_token, name="verify-token"),
] + router.urls
