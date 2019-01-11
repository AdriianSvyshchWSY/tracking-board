from .base import *

import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration


DEBUG = False

SHOW_DOCS = False

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['*']

sentry_sdk.init(dsn=os.environ['SENTRY_DSN'],
                integrations=[DjangoIntegration()])

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    'anymail',
)

EMAIL_BACKEND = 'anymail.backends.sendgrid.EmailBackend'
ANYMAIL = {'SENDGRID_API_KEY': os.getenv('SENDGRID_API_KEY')}
