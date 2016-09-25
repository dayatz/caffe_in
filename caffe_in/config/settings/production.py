from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get(
            "CAFFE_IN_DB_NAME",
            caffe_in),
        'USER': os.environ.get(
            "CAFFE_IN_DB_USERNAME",
            caffe_in),
        'PASSWORD': os.environ.get(
            "CAFFE_IN_DB_PASS",
            caffe_in),
        'HOST': os.environ.get(
            "CAFFE_IN_DB_HOST", 'localhost'),
        'PORT': os.environ.get(
            "CAFFE_IN_DB_PORT", '')
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.environ.get(
                "CAFFE_IN_LOG_DIR"),
                os.path.join(os.path.dirname(BASE_DIR), 'log.txt')),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
