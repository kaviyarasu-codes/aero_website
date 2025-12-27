import sys, os
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aero_website.settings")

application = get_wsgi_application()
