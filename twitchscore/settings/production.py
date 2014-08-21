# settings/production.py
from .base import *

#DEBUG
DEBUG = False
TEMPLATE_DEBUG = DEBUG
SESSION_SAVE_EVERY_REQUEST = False

ALLOWED_HOSTS = ['*']

#DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': '',
    }
}

#STATIC
STATIC_ROOT = root('static')

STATICFILES_DIRS = (
    root('files/media'),
)