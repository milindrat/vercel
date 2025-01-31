#!/bin/bash
set -o errexit   # Exit on the first error

python -m venv myenv
myenv\Scripts\activate
# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files without prompting for input
python manage.py collectstatic 

# Apply database migrations
python manage.py migrate

gunicorn Testing.wsgi:application