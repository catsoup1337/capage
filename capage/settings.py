import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'gq8t=4q6dndw=yuuum8cyz)-=tp!@qcty2l#d+@z!(lyzvm!wc'

DEBUG = True

ALLOWED_HOSTS = ['*']

CART_SESSION_ID = 'cart'


INSTALLED_APPS = [
    'cart',
    'posts',
    'accounts',
    'sorl.thumbnail',
    'phonenumber_field',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'storages',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'capage.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'capage.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
# STATIC_URL = '/static/'


prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'
SITE_ID=1
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = '/home/www/code/project1/capage/static/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# dstatic > dstatic > settings.py

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/posts/'

#STATICFILES_DIRS = [
#           os.path.join(BASE_DIR, "static"),
#           ]
