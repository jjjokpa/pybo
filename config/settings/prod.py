from .base import *
ALLOWED_HOSTS = ['18.182.179.243']

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = []

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'l-V6>bN_f*bns*7iue$t^^HGZh)8l2<0',
        'HOST': 'ls-a3ace6072aaa9e05783d86c1f924f9be446c717a.cwxistc3vjec.ap-northeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
