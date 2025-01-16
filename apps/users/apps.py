from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'  # This is the Python path to your app
    label = 'my_users' # This is the unique label (important!)