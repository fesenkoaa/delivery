import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-47l+8ul%wmgqat(v#r7t14*7lt3*5b(o-^_ry@c%r)4f60-&5@'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'grill_delivery',
        'USER': 'fesenkoaa',
        'PASSWORD': '231105',
        'HOST': 'localhost',
        'POST': ''
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]