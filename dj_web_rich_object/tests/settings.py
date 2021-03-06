"""
Configuration and launcher for Django Web Rich Object tests.
"""
import os
import tempfile
import dj_database_url

DEBUG = int(os.environ.get('DEBUG', '1'))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTAPP_DIR = os.path.join(BASE_DIR, 'testapp/')

ADMINS = (
    ('ham', 'foo@bar'),
)
ALLOWED_HOSTS = ['*']
MIDDLEWARE_CLASSES = MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'dj_web_rich_object.tests.urls'
SECRET_KEY = "it's a secret to everyone"
SITE_ID = 1
INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'dj_web_rich_object',
)

DATABASE = dj_database_url.config(default='sqlite:///test.sqlite')
DATABASES = {'default': DATABASE}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

SERVER_EMAIL = 'wro@test.org'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            )
        }
    },
]

STATIC_URL = '/static/'
MEDIA_ROOT = os.environ.get('MEDIA_ROOT') or tempfile.mkdtemp()
