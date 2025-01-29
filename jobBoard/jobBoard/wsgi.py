import os
from django.core.wsgi import get_wsgi_application

# Fix settings module path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobBoard.settings')

application = get_wsgi_application()
