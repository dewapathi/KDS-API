from .base import *

import os

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "kds_db"),
        "USER": os.environ.get("POSTGRES_USER", "kds"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "kds"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}
ALLOWED_HOSTS = ["*"]
