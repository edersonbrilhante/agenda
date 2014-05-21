"""
Django settings for agenda project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
from config import DB_SERVER, ENV
djcelery.setup_loader()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4m+ja8juz$f30=^(dio(xul_y_i$_gd6@d8w=woqmswrgkd!j='

# SECURITY WARNING: don't run with debug turned on in production!
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
    'agenda',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'agenda.urls'

WSGI_APPLICATION = 'agenda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
name =  os.path.join(BASE_DIR, 'db.sqlite3')
if DB_SERVER[ENV]["name"]:
    name =  DB_SERVER[ENV]["name"]

DATABASES = {
    'default': {
        'ENGINE': DB_SERVER[ENV]["engine"],
        'NAME': name,
      'USER': DB_SERVER[ENV]["user"],                      # Not used with sqlite3.
        'PASSWORD': DB_SERVER[ENV]["password"],                  # Not used with sqlite3.
        'HOST': DB_SERVER[ENV]["host"],                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': DB_SERVER[ENV]["port"],                      # Set to empty string for default. Not used with sqlite3.
   
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
