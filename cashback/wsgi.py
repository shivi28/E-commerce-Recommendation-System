"""
WSGI config for cashback project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# Whitenoise import has changed in newer versions
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cashback.settings")

application = get_wsgi_application()
# Whitenoise application has changed in newer versions
# application = DjangoWhiteNoise(application)
