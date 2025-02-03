from waitress import serve
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)
