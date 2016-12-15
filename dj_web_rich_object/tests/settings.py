"""
Configuration and launcher for Django Web Rich Object tests.
"""
import os
import tempfile
import dj_database_url

DEBUG = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTAPP_DIR = os.path.join(BASE_DIR, 'testapp/')

ADMINS = (
    ('ham', 'foo@bar'),
)
ALLOWED_HOSTS = ['*']
MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = 'dbbackup.tests.testapp.urls'
SECRET_KEY = "it's a secret to everyone"
SITE_ID = 1
MEDIA_ROOT = os.environ.get('MEDIA_ROOT') or tempfile.mkdtemp()
INSTALLED_APPS = (
    'dj_web_rich_object',
)

DATABASE = dj_database_url.config(default='sqlite:///%s' %
                                  tempfile.mktemp())
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
    },
]
