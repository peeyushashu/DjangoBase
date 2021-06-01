from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip-address','www.your-website.com']


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'Our_DB_name',
        'USER': '',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':''
    }
}

STRIPE_PUBLIC_KEY='LIVE_PUBLIC_KEY'
STRIPE_SECRET_KEY='LIVE_SECRET_KEY'