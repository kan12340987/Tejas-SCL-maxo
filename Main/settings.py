"""
Django settings for Main project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u+1nty8^qky#f^*(1mlb3*&yexub%97&x1h=337%wn-&p_ga7o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'noterepo.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'Users.apps.UsersConfig',
    'webapp.apps.WebappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here 
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = (
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    
    'django.contrib.auth.backends.ModelBackend',
)





SOCIAL_AUTH_FACEBOOK_KEY = '4227417197288163'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8acd3368e65e0db2560c4d32878c5837'



SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '157532831349-8tjlhngkdjh4l4l0pd1lr0n5g6lb6sfo.apps.googleusercontent.com'  # App ID
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'r0kG1Kogold5IsRgCoE3pX3m'


SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY  = '86qlnzqoeqfd6y'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET ='rrkWOX1KfiTo2hmz'


SOCIAL_AUTH_TWITTER_KEY= '7pa31RhcmhXKnx2g0crlnf1Cy'
SOCIAL_AUTH_TWITTER_SECRET= '2186gnzdijyLxeTWGISsABMIqd4nTNXyEFpTJpfmYEj99dgZAb'



SOCIAL_AUTH_GITHUB_KEY= 'c4c502001ba6c80b9054'
SOCIAL_AUTH_GITHUB_SECRET= '0af3611cc2a1eb7753e457d3e5295b41f17b137d'
SOCIAL_AUTH_GITHUB_SCOPE = ['email']



WSGI_APPLICATION = 'Main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = './Users-Homepage'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True






# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_URL = 'Users-home'
LOGIN_REDIRECT_URL = 'Users-home'
