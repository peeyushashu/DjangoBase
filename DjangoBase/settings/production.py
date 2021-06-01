from .base import *

DEBUG = config('DEBUG', cast=bool)
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
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD':config('DB_PASS'),
        'HOST':config('DB_HOST'),
        'PORT':config('DB_PORT')
    }
}

STRIPE_PUBLIC_KEY= config('LIVE_SECRET_KEY')
STRIPE_SECRET_KEY=config('LIVE_PUBLIC_KEY')