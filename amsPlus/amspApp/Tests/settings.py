"""

mysqldbcopy --source=root:009100@localhost --destination=root:009100@localhost amsp:amspTest

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jp20ia%=42cm@4%f7(2!ppwkg^c6sovc2y9j=-a($8$i(46g+t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGGING_CONFIG = None

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_CHARSET = "utf-8"
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
DEFAULT_INDEX_TABLESPACE = ""
DEFAULT_TABLESPACE = ""
ABSOLUTE_URL_OVERRIDES = {}
FORCE_SCRIPT_NAME = None
DEBUG_PROPAGATE_EXCEPTIONS = False
DEFAULT_EXCEPTION_REPORTER_FILTER = "django.views.debug.SafeExceptionReporterFilter"
FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.MemoryFileUploadHandler",
                        "django.core.files.uploadhandler.TemporaryFileUploadHandler")
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
SECURE_PROXY_SSL_HEADER = None
USE_X_FORWARDED_HOST = False
DECIMAL_SEPARATOR = "."
NUMBER_GROUPING = 0
THOUSAND_SEPARATOR = ","
USE_THOUSAND_SEPARATOR = False

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
    'amspApp',
    'amspApp.amspUser',
    'amspApp.CompaniesManagment',

)

AUTH_USER_MODEL = 'amspUser.MyUser'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
        'NAME': 'amspTest',
        'USER': 'root',
        'HOST': 'localhost',
        'PASSWORD': '009100',
    },
}


from mongoengine import connect
connect("amsPlus")




ROOT_URLCONF = 'amsp.urls'

WSGI_APPLICATION = 'amsp.wsgi.application'

MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

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

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)