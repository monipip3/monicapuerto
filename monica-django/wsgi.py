"""
WSGI config for monicapuerto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monicapuerto.settings")

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

#Excerpt From: Tracy Osborn. “Hello Web App.” iBooks. 
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monicapuerto.settings")

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)