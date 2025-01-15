from pathlib import Path
from django.conf.global_settings import (
    INSTALLED_APPS, AUTH_USER_MODEL, LANGUAGE_CODE, SECRET_KEY, DEBUG,
    ALLOWED_HOSTS, MIDDLEWARE, TEMPLATES, WSGI_APPLICATION, AUTH_PASSWORD_VALIDATORS,
    LOCALE_PATHS, TIME_ZONE, USE_I18N, USE_L10N, USE_TZ, STATIC_URL, MEDIA_URL,
    MEDIA_ROOT, DEFAULT_AUTO_FIELD
)

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'what-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'startautotheorie',         # Replace with your PostgreSQL database name
        'USER': 'postgres',         # Replace with your PostgreSQL username
        'PASSWORD': 'I AM NOT SURE ABOUT MY PW', # Replace with your PostgreSQL password
        'HOST': 'localhost',                  # Or the IP address of your database server
        'PORT': '5432',                       # Default PostgreSQL port
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users', #User management app
    'apps.practice', #Driving theory app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware', # Locale middleware for translations

]

ROOT_URLCONF = 'start_auto_theorie.urls'

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
                ],
            },
        },
    ]

WSGI_APPLICATION = 'start_auto_theorie.wsgi.application'

AUTH_USER_MODEL = 'users.CustomUser'

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

LANGUAGE_CODE = 'nl'

LOCALE_PATHS = [
    BASE_DIR/'locale'
]

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/' # Adjust this URL if your login page is different

STATICFILES_DIRS = [BASE_DIR/'static']