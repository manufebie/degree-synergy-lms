from .base import *

DEBUG = True

INSTALLED_APPS += {
    'debug_toolbar',
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}

INTERNAL_IPS = ['127.0.0.1']

# Static stuff

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'assets')]

