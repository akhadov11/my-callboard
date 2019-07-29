"""
Directories & files & paths settings.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REPO_DIR = os.path.dirname(BASE_DIR)

DEPLOY_DIR = os.path.join(BASE_DIR, "deploy")

ROOT_URLCONF = "apps.core.urls"

WSGI_APPLICATION = "wsgi.application"

STATIC_URL = "/static/"

MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(DEPLOY_DIR, "static-root")

MEDIA_ROOT = os.path.join(DEPLOY_DIR, "media-root")

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

UPLOAD_FOLDER = "uploads/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

SILKY_PYTHON_PROFILER_RESULT_PATH = os.path.join(DEPLOY_DIR, "profiling_logs")
