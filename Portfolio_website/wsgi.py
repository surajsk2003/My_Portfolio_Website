import os
import sys

path = '/home/Suraj0Singh/My_Portfolio_Website'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'your_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
