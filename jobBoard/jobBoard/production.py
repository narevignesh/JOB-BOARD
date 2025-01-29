from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# Debug should be False in production
DEBUG = False

# Allowed hosts (replace with your production domain)
ALLOWED_HOSTS = ['Job-Board.com', 'www.Job-Board.com']  # Add your production domains

# Additional production settings, like security configurations
