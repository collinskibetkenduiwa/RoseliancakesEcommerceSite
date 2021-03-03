from .base import *
DEBUG=True
ALLOWED_HOSTS=['*']
MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',#metrics  
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',#admin doc bookmarklets
    'django.contrib.auth.middleware.AuthenticationMiddleware',#two factor authentication
    'django_otp.middleware.OTPMiddleware',#two factor authentication
    'oscar.apps.basket.middleware.BasketMiddleware',#basket 
    'django_user_agents.middleware.UserAgentMiddleware',#adding user agent attribute to the  request
    'django_prometheus.middleware.PrometheusAfterMiddleware',#metrics
    'simple_pages.middleware.PageFallbackMiddleware',#added pages
    
]


######################################Fixtures###############################
FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)

# if  DEBUG:
#     STATIC_ROOT = os.path.join(BASE_DIR, '/static')
# # else:
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
OSCAR_HOMEPAGE='/home'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}