from django.conf.global_settings import INSTALLED_APPS, AUTH_USER_MODEL

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
    'apps.users',
    'apps.practice',
]

AUTH_USER_MODEL = 'users.CustomUser'

