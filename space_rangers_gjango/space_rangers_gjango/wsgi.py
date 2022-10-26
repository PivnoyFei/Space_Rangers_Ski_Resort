import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'space_rangers_gjango.settings')

application = get_wsgi_application()
