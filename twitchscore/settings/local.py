# settings/local.py
from .base import *

#DEBUG
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = []

#DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': '',
    },
    'dump': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dump_db',
        'USER': 'postgres',
        'PASSWORD': '',
    }
}

#TEMPLATE
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)