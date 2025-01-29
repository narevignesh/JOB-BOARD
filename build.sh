#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Navigate to Django project directory
cd jobBoard

# Collect static files
python manage.py collectstatic --no-input

# Make fresh migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate 