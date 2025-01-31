#!/bin/bash
set -o errexit   # Exit on the first error


# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files without prompting for input
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

gunicorn Testing.wsgi:application