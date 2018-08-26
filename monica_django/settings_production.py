#inherit the standard settings file for defaults

from monica_django.settings import *


#Everything below will override our standard settings:


#parse database configuration from $DATABASE_URL

import dj_database_url

DATABASES['default'] = dj_database_url.config()


#Honor the 'X-Forwaded Proto' header for request.is_secure()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')


#Allow all host headers

ALLOWED_HOSTS = ['*']

#Set debug to false

DEBUG = False 

#static asset configuration

STATICFILES_STORAGE = \
'whitenoise.storage.CompressedManifestStaticFilesStorage'