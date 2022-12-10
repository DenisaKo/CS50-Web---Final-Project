"""
WSGI config for working_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'working_system.settings')

# https://stackoverflow.com/questions/573618/set-up-a-scheduled-job
def ready():
        from jobs import updater
        updater.start()

application = get_wsgi_application()
