import os
from settings.base import *

SECRET_KEY = os.environ.get('SECRET_KEY', 'default')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "172.17.0.1",
        "PORT": "password",
    }
}
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

# let's speed up tests a little
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
