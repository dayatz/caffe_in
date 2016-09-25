from .base import *
from .apps import INSTALLED_APPS

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions'
]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'caffe_in.sqlite3'),
#     }
# }

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get(
            "CAFFE_IN_DB_NAME",
            'caffe_in'),
        'USER': os.environ.get(
            "CAFFE_IN_DB_USERNAME",
            'caffe_in'),
        'PASSWORD': os.environ.get(
            "CAFFE_IN_DB_PASS",
            'caffe_in'),
        'HOST': os.environ.get(
            "CAFFE_IN_DB_HOST", 'localhost'),
        'PORT': os.environ.get(
            "CAFFE_IN_DB_PORT", '')
    }
}
