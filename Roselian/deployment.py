from .base import *

DEBUG=False

ALLOWED_HOSTS = ['www.roseliancakes.co.ke','roseliancakes.co.ke','127.0.0.1']

#################################################################
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',#metrics  
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',#cache
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',#cache
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',#admin doc bookmarklets
    'django.contrib.auth.middleware.AuthenticationMiddleware',#two factor authentication
    'django_otp.middleware.OTPMiddleware',#two factor authentication
    # Ensure a valid basket is added to the request instance for every request
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',#adding user agent attribute to the  request
    'django_prometheus.middleware.PrometheusAfterMiddleware',#metrics
    'simple_pages.middleware.PageFallbackMiddleware',# added pages
    'django.middleware.cache.FetchFromCacheMiddleware',#cache
    
    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config('NAME'),
        'USER':config('USER'),
        'PASSWORD':config('PASSWORD'),
        'HOST':config('HOST'),
        'PORT': '',
    }
}


# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# CACHE_MIDDLEWARE_ALIAS ="Roselian cakes"
# CACHE_MIDDLEWARE_SECONDS =60*60*60*24*7

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://658d791d6f8446c78a801ba97e94cac0@o414324.ingest.sentry.io/5303584",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)