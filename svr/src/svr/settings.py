"""
Django settings for svr project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

_redis_ip = os.environ.get('REDIS_IP', '127.0.0.1')
_redis_port = os.environ.get('REDIS_PORT', '6379')

# Celery setting
CELERY_BROKER_URL = 'redis://{}:{}/0'.format(_redis_ip, _redis_port)
# CELERY_RESULT_BACKEND = 'redis://{}'.format(_redis_ip)

# Channel
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "svr.routing.channel_routing",
    },
}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@c-0i&)0qa33ht((#m1x@b4=px^0dq_y+w1$c@7=jp%tihu(#t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.sessions',
    'rest_framework',
    'app.apps.AppConfig',
    'channels',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
]

ROOT_URLCONF = 'svr.urls'

TEMPLATES = []

WSGI_APPLICATION = 'svr.wsgi.application'


# Session
# https://docs.djangoproject.com/en/1.11/ref/settings/#sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Cache
# https://docs.djangoproject.com/en/1.11/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://{}:{}/1'.format(_redis_ip, _redis_port),
    },
}


# Logging
# https://docs.djangoproject.com/en/1.11/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'detail': {
            'format': '%(asctime)s:[%(levelname)s][%(module)s:%(lineno)d][%(funcName)s]:%(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': [],
            'class': 'logging.StreamHandler',
            'formatter': 'detail'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'filters': []
        },
        'django': {
            'handlers': ['console'],
            'propagate': False,
        },
    }
}


# rest_framework
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
    ),
    'DEFAULT_PERMISSION_CLASSES': (
    ),
    'UNAUTHENTICATED_USER': None,
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'NON_FIELD_ERRORS_KEY': 'non_field_errors',
}
