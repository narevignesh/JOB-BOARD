import os
from django.core.wsgi import get_wsgi_application

# Set the settings module based on the environment
# This will use 'jobBoard.settings.production' when deploying, or 'jobBoard.settings' for development
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobBoard.settings.production')

application = get_wsgi_application()
