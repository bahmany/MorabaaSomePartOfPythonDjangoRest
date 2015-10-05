"""
Django settings for bmps project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_mongoengine',
    'amspApp.Infrustructures',
    'amspApp',
    'amspApp.amspUser',
    'amspApp.CompaniesManagment',
    'amspApp.CompaniesManagment.Charts',
    'amspApp.CompaniesManagment.Positions',
    'amspApp.CompaniesManagment.Secretariat',
    'amspApp.MyProfile',
    'amspApp.FileServer',
    'amspApp.Friends',
)

AUTH_USER_MODEL = 'amspUser.MyUser'


LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Iran'
USE_TZ = True
LANGUAGES = (
    ('en', 'English'),
    ('fa', 'Farsi'),
)

Temp_Path = os.path.realpath('.')

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'amspApp/cache'),
        'TIMEOUT': 3600,
        'ALIAS': "default",
        'KEY_PREFIX': "default",
        'OPTIONS': {
            'MAX_ENTRIES': 5000
        }
    }
}

CACHE_MIDDLEWARE_ALIAS = "default"


MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'amspApp.Authentication.AnonymouseChecker.LoginRequiredMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'amspApp.middlewares.TimezoneMiddleware.TimezoneMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
    }
}

from mongoengine import connect
connect("amsPlus")

ROOT_URLCONF = 'amsp.urls'

LOGIN_URL = "/#/login"
LOGIN_EXEMPT_URLS = (
 r'^about\.html$',
 r'^legal/', # allow the entire /legal/* subsection
)

WSGI_APPLICATION = 'amsp.wsgi.application'

MEDIA_ROOT = os.path.join(BASE_DIR,  'images')
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


# SESSION_COOKIE_AGE = 1209600
# SESSION_COOKIE_NAME = 'morabaaPlus'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)




USE_EMAIL_VERIFICATION_FOR_REGISTRATION = True




