
set -o errexit

pip install -r requiremetns.txt

py manage.py collectstatic --no-input
 
py manage.py migrate 