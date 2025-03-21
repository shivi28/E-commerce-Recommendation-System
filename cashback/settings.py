"""
Django settings for cashback project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import dj_database_url
import os
from sys import path
#import djcelery
#djcelery.setup_loader()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGIN_URL = '/user_login/login'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't@n&rj2f23fs-okhulap7a!jf3(k@uw=25_ju_5lv=m-p=x6-y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CELERY_BROKER_URL = 'amqp://localhost//'

#Broker settings
BROKER_URL = "localhost"
#BROKER_PORT = 5672
BROKER_USER = ""
BROKER_PASSWORD = ""
#BROKER_VHOST = "/"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'user_login',
#    'djcelery',
]

# Updated from MIDDLEWARE_CLASSES to MIDDLEWARE for Django 1.11+
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise middleware for serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Keep MIDDLEWARE_CLASSES for backward compatibility
MIDDLEWARE_CLASSES = MIDDLEWARE

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.docarto.com'
EMAIL_HOST_USER = 'madhurmadhur@docarto.com'
EMAIL_HOST_PASSWORD = 'madhur123'
#EMAIL_PORT = '465'
#EMAIL_USE_TLS = True
# The default_from_email is required, it was missing so we were not able to send email for forgot password using password_reset in
# django.contrib.auth.views. Perhaps it was the problem due to which we were not able to send email during sign up using send_mail()
DEFAULT_FROM_EMAIL  = 'madhurmadhur@docarto.com'
#SERVER_EMAIL    = 'root@docarto.com'

ROOT_URLCONF = 'cashback.urls'

TEMPLATES = [
    {
        #'TEMPLATE_DIRS' : os.path.join(BASE_DIR, 'templates'),
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



WSGI_APPLICATION = 'cashback.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Update database configuration with $DATABASE_URL.
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)

#database configuration on docarto1 server
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'docarto1_cashback',
#        'USER': 'docarto1_madhur',
#        'PASSWORD': 'madhur123',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
#}

#database configuration on local server to access docarto1 database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'docarto1_cashback',
#        'USER': 'docarto1_madhur',
#        'PASSWORD': 'madhur123',
#        'HOST': 'docarto1.wwwss28.a2hosted.com',
#        'PORT': '',
#    }
#}

#database configuration on heroku server to access  database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'd42k7k6ht5is5h',
#        'USER': 'tcgmlnuebvpsua',
#        'PASSWORD': '7b1dc5731b298efe3ea3a5d3f78cafd1a36c77346dd4a80d5e41f7bf0ff82568',
#        'HOST': 'ec2-50-17-217-166.compute-1.amazonaws.com',
#        'PORT': '5432',
#    }
#}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'd57t6af2cug8v3',
#        'USER': 'uuwegnsdcoymbt',
#        'PASSWORD': 'de840ec3a5fa9064907149a2ce3dddfa9cd8f32b99aeb4e197e8528e046242cf',
#        'HOST': 'ec2-54-221-207-192.compute-1.amazonaws.com',
#        'PORT': '5432',
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# static files settings on local machine
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


MEDIAFILES_DIRS = (MEDIA_ROOT)

# static files docartoc settings on server (Perhaps media_url and media_root can be like static_url and static _root i.e. url/path to media
#directory on server)
#STATIC_URL = 'http://docarto1.wwwss28.a2hosted.com/cashback/public/static/'
#STATIC_ROOT = '/home/docarto1/public_html/cashback/public/static/'
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#static files settings on local to access static files from server
#STATIC_URL = 'http://docarto.com/cashback/public/static/'
#STATIC_ROOT = '/home/docarto1/public_html/cashback/public/static/'
#MEDIA_URL = 'http://docarto.com/cashback/media/'
#MEDIA_ROOT = '/home/docarto1/public_html/cashback/media/'
