"""
Django settings for trello_reporter project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5n_v*opwlu_u@i1nw=rdheam4#hr+1$x93_qj2go5jhb5u&q-7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INTERNAL_IPS = ['172.17.0.1', '127.0.0.1', '::1']
ALLOWED_HOSTS = ['172.17.0.1', '127.0.0.1']
DEBUG_TOOLBAR_PATCH_SETTINGS = False

AUTH_USER_MODEL = "authentication.TrelloUser"
AUTHENTICATION_BACKENDS = (
    "trello_reporter.authentication.backend.TrelloAuthBackend",
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'trello_reporter.charting',
    'trello_reporter.authentication',  # not to conflict with django.c.auth
    'trello_reporter.harvesting',
    'trello_reporter.static_data',  # used for easier development
    'django_extensions',
    'debug_toolbar',
    # 'channels',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'trello_reporter.authentication.middleware.TrelloAuthMiddleware',
    'trello_reporter.authentication.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'trello_reporter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'trello_reporter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["POSTGRESQL_DATABASE"],
        'USER': os.environ["POSTGRESQL_USER"],
        'PASSWORD': os.environ["POSTGRESQL_PASSWORD"],
        'HOST': "db"
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s\t%(asctime)s\t%(filename)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': "verbose",
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'trello_reporter': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        }
    },
}

# Application settings

try:
    API_KEY = os.environ["API_KEY"]
except KeyError:
    raise ImproperlyConfigured(
        "Developer API key not found, please obtain it from:\n"
        "https://trello.com/app-key\n"
        "and set it as environment variable 'API_KEY'"
    )
