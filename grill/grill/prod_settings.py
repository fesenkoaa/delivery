import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-47l+8ul%wmgqat(v#r7t14*7lt3*5b(o-^_ry@c%r)4f60-&5@'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'delivery',
        'USER': 'user_db',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'POST': '5432'
    }
}

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')