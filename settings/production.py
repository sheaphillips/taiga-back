from .common import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_SERVICE_NAME', ''),
        'PORT': '5432',
    }
}

# MEDIA_URL = "http://example.com/media/"
# STATIC_URL = "http://example.com/static/"
# SITES["front"]["scheme"] = "http"
# SITES["front"]["domain"] = "example.com"

DEBUG = False
# PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = os.environ.get('TAIGA_FROM_EMAIL_ADDRESS', 'no-reply@example.com')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#CELERY_ENABLED = True

# EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
# EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:PASSWORD_FOR_EVENTS@localhost:5672/taiga"}

# Uncomment and populate with proper connection parameters
# for enable email sending. EMAIL_HOST_USER should end by @domain.tld
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = False
EMAIL_HOST = os.environ.get('TAIGA_EMAIL_HOST','')
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 25

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"
