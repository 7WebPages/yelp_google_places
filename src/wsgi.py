import os
from os.path import abspath, dirname, realpath
from sys import path

path.insert(1, dirname(realpath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.conf")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
