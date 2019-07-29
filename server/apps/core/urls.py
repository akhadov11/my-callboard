"""
Root urls.
"""
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.shortcuts import render
from django.conf.urls.static import static

from rest_framework_swagger.views import get_swagger_view

from apps.api.views import GraphQLView

admin.site.site_header = "Administration"
admin.site.site_title = "Administration"

SCHEMA_VIEW = get_swagger_view(title="API")


def home(request):
    return render(request, "home.html")


urlpatterns = [
    path("", home),
    path("api/", include("apps.api.urls", namespace="api")),
    path("graphql/", GraphQLView.as_view(graphiql=False)),
]

if settings.ADMIN_PANEL_AVAILABLE:
    urlpatterns += [path("admin/", admin.site.urls)]

if settings.SHOW_API_DOCS:
    urlpatterns += [
        path("swagger/", SCHEMA_VIEW, name="swagger"),
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    ]

if settings.SHOW_GRAPHIQL:
    urlpatterns += [path("graphiql/", GraphQLView.as_view(graphiql=True))]

if settings.DEBUG and settings.SILK_PROFILING:
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]

if settings.SERVE_STATIC_IN_APP:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
