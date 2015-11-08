"""
WSGI config for shwipe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
https://devcenter.heroku.com/articles/django-assets
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shwipe.settings")

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
