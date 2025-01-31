#!/bin/bash
set -o errexit   # Exit on the first error

PORT=${PORT:-8000}
# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files without prompting for input
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

exec gunicorn Testing.wsgi:application --bind 0.0.0.0:$PORT