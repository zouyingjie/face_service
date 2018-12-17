"""
Django settings for FaceIdService project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '75qa_xj0s@eb7p1$@yzgvm1f$%_p36rd4dp-(vzy9e6*xc28cf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', "101.236.34.86", 'facetest.qingchengfit.cn']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "face",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'settings.urls'

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(pathname)s '
                      '%(lineno)s %(funcName)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'info': {
            '()': 'libs.logs.InfoFilter',
        },
        'warning': {
            '()': 'libs.logs.WarningFilter',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'sentry': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.raven_compat.'
                     'handlers.SentryHandler',
        },
        'project_info': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': "{PROJECT_HOME}/data/logs/info.log".
            format(PROJECT_HOME=PROJECT_HOME),
            'formatter': 'verbose',
            'filters': ['require_debug_false', 'info'],
        },
        'project_warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': "{PROJECT_HOME}/data/logs/warning.log".
            format(PROJECT_HOME=PROJECT_HOME),
            'formatter': 'verbose',
            'filters': ['require_debug_false', 'warning'],
        },

    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'project_info',
                         'project_warning', 'sentry'],
        },

        'libs': {
            'level': 'DEBUG',
            'handlers': ['console', 'project_info',
                         'project_warning', 'sentry'],
            'propagate': False,
        },

        'django': {
            'level': 'ERROR',
            'handlers': ['console', 'project_info',
                         'project_warning', 'sentry'],
            'propagate': False,
        },

        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    },
}
