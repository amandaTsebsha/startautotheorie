import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'start_auto_theorie.settings')

application = get_wsgi_application()

