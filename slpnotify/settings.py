"""
Django settings for x project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decouple import config
import redis
import psycopg2
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g7+b)g5r@ugo4&ix$mto0b(u*^9_51p5a5-j#_@t)1g!fv&j99'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'slpnotify.scibizinformatics.com',
    'localhost',
    '*'
]

# Application definition

INSTALLED_APPS=[
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'rest_framework',
'rest_framework.authtoken',
'corsheaders',
'main',
'django.contrib.admin',
'drf_yasg'
]

MIDDLEWARE=[
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'corsheaders.middleware.CorsMiddleware',

'whitenoise.middleware.WhiteNoiseMiddleware',

'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'slpnotify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'slpnotify.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_DB', default='slpnotify'),
        'HOST': config('POSTGRES_HOST', default='localhost'),
        'PORT': config('POSTGRES_PORT', default=5432, cast=int),
        'USER': config('POSTGRES_USER', default='postgres'),
        'PASSWORD': config('POSTGRES_PASSWORD', default='badpassword'),
        'OPTIONS': {
            'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



DB_NUM = [0,1,3]
REDIS_HOST = config('REDIS_HOST', default='localhost')
REDIS_PASSWORD = config('REDIS_PASSWORD', default='')
REDIS_PORT = config('REDIS_PORT', default=6379)
CELERY_IMPORTS = ('main.tasks',)

if REDIS_PASSWORD:
    CELERY_BROKER_URL = 'redis://user:%s@%s:%s/%s' % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, DB_NUM[0])
    CELERY_RESULT_BACKEND = 'redis://user:%s@%s:%s/%s' % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, DB_NUM[1])
    REDISKV = redis.StrictRedis(
        host=REDIS_HOST,
        password=REDIS_PASSWORD,
        port=6379,
        db=DB_NUM[2]
    )
else:
    CELERY_BROKER_URL = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, DB_NUM[0])
    CELERY_RESULT_BACKEND = 'redis://%s:%s/%s' % (REDIS_HOST, REDIS_PORT, DB_NUM[1])
    REDISKV = redis.StrictRedis(
    host=REDIS_HOST,
    port=6379,
    db=DB_NUM[2]
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

CELERY_TASK_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 5

CELERY_BEAT_SCHEDULE = {
    'latest_blockheight_getter': {
        'task': 'main.tasks.latest_blockheight_getter',
        'schedule': 5
    },
    'second_blockheight_scanner': {
        'task': 'main.tasks.second_blockheight_scanner',
        'schedule': 60
    },
    'first_blockheight_scanner': {
        'task': 'main.tasks.first_blockheight_scanner',
        'schedule': 120
    },
    'slpdb_token_scanner': {
        'task': 'main.tasks.slpdb_token_scanner',
        'schedule': 600
    },
    'openfromredis': {
        'task': 'main.tasks.openfromredis',
        'schedule': 300
    },
    'slpbitcoinsocketsocket': {
        'task': 'main.tasks.slpbitcoinsocket',
        'schedule': 21
    },
    'bitsocket': {
        'task': 'main.tasks.bitsocket',
        'schedule': 29
    },
    'bitdbquery': {
        'task': 'main.tasks.bitdbquery',
        'schedule': 300
    },
    'updates': {
        'task': 'main.tasks.updates',
        'schedule': 4800
    }
}

CORS_ORIGIN_WHITELIST = [
    "https://tokensale-staging.scibizinformatics.com",
    "https://tokensale.scibizinformatics.com"
]

if DEBUG:
    CORS_ORIGIN_WHITELIST += ['http://localhost:8000']


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}

ACCESS_TOKEN_LIFETIME = int(config("ACCESS_TOKEN_LIFETIME", "0"))
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=ACCESS_TOKEN_LIFETIME or 1)
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "JWT": {
            "description": 'Input as "Bearer <token_here>"',
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
        }
    },
}

#Telegram bot settings
TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', default='')
TELEGRAM_BOT_USER = config('TELEGRAM_BOT_USER', default='')
TELEGRAM_DESTINATION_ADDR = 'https://slpnotify.scibizinformatics.com/telegram/notify/'


# Slack credentials and configurations

SLACK_BOT_USER_TOKEN = config('SLACK_BOT_USER_TOKEN', default='')
SLACK_VERIFICATION_TOKEN = config('SLACK_VERIFICATION_TOKEN', default='')
SLACK_CLIENT_ID = config('SLACK_CLIENT_ID', default='')
SLACK_CLIENT_SECRET = config('SLACK_CLIENT_SECRET', default='')
SLACK_SIGNING_SECRET = config('SLACK_SIGNING_SECRET', default='')

SLACK_DESTINATION_ADDR = 'https://slpnotify.scibizinformatics.com/slack/notify/'
SLACK_THEME_COLOR = '#82E0AA'
