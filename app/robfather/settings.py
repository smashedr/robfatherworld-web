import os
from distutils.util import strtobool

ROOT_URLCONF = 'robfather.urls'
WSGI_APPLICATION = 'robfather.wsgi.application'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_DIR = os.environ['DJANGO_DATA_DIR']

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
LOGIN_URL = '/oauth/'
LOGIN_REDIRECT_URL = '/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates')]

SESSION_COOKIE_AGE = int(os.getenv('DJANGO_SESSION', 1209600))
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED', '*').strip('"').split(' ')
DEBUG = bool(strtobool(os.getenv('DJANGO_DEBUG', 'True')))
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
STATIC_ROOT = os.getenv('DJANGO_STATIC_DIR')
MEDIA_ROOT = os.getenv('DJANGO_MEDIA_DIR')

DATETIME_FORMAT = os.getenv('DJANGO_DATETIME_FORMAT', 'N j, Y, f A').strip('"')
TIME_ZONE = os.getenv('TZ', 'America/Los_Angeles')
LANGUAGE_CODE = os.getenv('DJANGO_LANGUAGE_CODE', 'en-us')

TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')
TWITCH_REDIRECT_URI = os.getenv('TWITCH_REDIRECT_URI')
TWITCH_GRANT_TYPE = os.getenv('TWITCH_GRANT_TYPE')
TWITCH_SCOPE = os.getenv('TWITCH_SCOPE')

USE_I18N = True
USE_L10N = True
USE_TZ = True

if DEBUG:
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    def show_toolbar(request):
        return True if request.user.is_staff else False

    DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': show_toolbar}

if 'DJANGO_DEV_DB' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(DATA_DIR, os.environ['DJANGO_DEV_DB']),
            'NAME': os.path.join(BASE_DIR, os.environ['DJANGO_DEV_DB']),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['DATABASE_NAME'],
            'USER': os.environ['DATABASE_USER'],
            'PASSWORD': os.environ['DATABASE_PASS'],
            'HOST': os.environ['DATABASE_HOST'],
            'PORT': os.environ['DATABASE_PORT'],
            'OPTIONS': {
                'isolation_level': 'repeatable read',
                'init_command': "SET sql_mode='STRICT_ALL_TABLES'",
            },
        }
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(levelname)s - %(filename)s %(module)s.%(funcName)s:%(lineno)d - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
        'app': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_APP_LOG_LEVEL', 'DEBUG'),
            'propagate': True,
        },
    },
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'home',
    'videos',
    'oauth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

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
