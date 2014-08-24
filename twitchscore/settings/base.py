import os
from os.path import join, abspath, dirname

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

#PATH CONFIGURATION
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

#MANAGER CONFIGURATION
ADMINS = (
    ('Alexander Nelzin', 'asnelzin@gmail.com'),
)

MANAGERS = ADMINS

#GENERAL CONFIGURATION
TIME_ZONE = 'UTC'
DEFAULT_CHARSET = 'utf-8'
LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = False
USE_L10N = True

#MEDIA
MEDIA_ROOT = root('media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

#STATIC FILES
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

#TEMPLATE
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    root('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    'django.core.context_processors.request',
)

#MIDDLWARE
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

#APP
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'south',
    'kombu.transport.django',
    'djcelery',

    'twitchscore.apps.accounts',
    'twitchscore.apps.stats'
)

#LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        }
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '%s/main.log' % root('./logs'),
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'twitchscore': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        }
    }
}

#URL
ROOT_URLCONF = 'twitchscore.urls'

#KEY
SECRET_KEY = get_env_variable('SECRET_KEY')

#CELERY
import djcelery
djcelery.setup_loader()

BROKER_URL = 'django://'

CELERY_TIMEZONE = TIME_ZONE

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'update_games': {
        'task': 'twitchscore.apps.stats.tasks.update_games',
        'schedule': crontab(minute='*/1'),
    }
}

#OTHER
WSGI_APPLICATION = 'twitchscore.wsgi.application'
RIOT_API_KEY = get_env_variable('RIOT_API_KEY')