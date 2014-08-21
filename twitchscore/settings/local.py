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
        'PASSWORD': 'podushka',
    }
}

#STATIC
STATICFILES_DIRS = (
    root('twitchscore/static'),
)

#TEMPLATE
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

#KEY
SECRET_KEY = '1r$5)d@+s#tks&wk^r&lxyeif3tnsbjh=^9z@ttmasm^n6w#wz'