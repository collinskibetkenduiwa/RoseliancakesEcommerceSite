import django
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.apps import apps
from django.conf.urls import include, url  # < Django-2.0
from django.urls import include, path  # > Django-2.0
from django.contrib import admin  
from django.views.i18n import JavaScriptCatalog
from oscar.views import handler403, handler404, handler500
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from django_otp.admin import OTPAdminSite #otp
from django_otp.plugins.otp_totp.models import TOTPDevice#otp
from location import views as locationviews

class OTPAdmin(OTPAdminSite):
    pass
admin_site=OTPAdmin(name='OTPAdmin')
#  end of two factor authentication.
# Call SiteMap properties
from base.sitemaps import Main_Pages
from base.sitemaps import CategorySitemap
from base.sitemaps import OtherPages
from base.sitemaps import ProductSitemap
from organizations.backends import invitation_backend
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0
    
# from base import 
sitemaps = {
    'Main_Pages':Main_Pages,
    'Products':ProductSitemap,
    'Categories':CategorySitemap,
    'Pages':OtherPages
    # 'Pages':Pages,
}
# from apps.sitemaps import base_sitemaps
admin.autodiscover()
urlpatterns = [
    path('', include('pwa.urls')), # You MUST use an empty string as the URL prefix for progressive web app
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    # i18n URLS need to live outside of i18n_patterns scope of Oscar
    path('i18n/', include('django.conf.urls.i18n')),
    path('roselian/admin', admin.site.urls),
    path('', apps.get_app_config("oscar_promotions").urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('admin/', include('smuggler.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('roselian/admin', admin_site.urls),
    path('', include('pages.urls'),name='pages'),
    path('',include('mpesa.urls'),name='mpesa'),
    path("dashboard/promotions/", apps.get_app_config("oscar_promotions_dashboard").urls),
    # Django auto generate sitemap.xml file
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path("api/", include("oscarapi.urls")),
    path('', include('mobile_delivery.urls')),
    path('sms', include('sms.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('newsletter/', include('newsletter.urls')),
    path('helpdesk/', include('helpdesk.urls')),
    path('prometheus/', include('django_prometheus.urls')),
    path('robots.txt', include('robots.urls')),#robots
    path('pages/', include('pages.urls'),name='pages'),
    path('contact', include('pages.urls'),name='contact'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('hijack/', include('hijack.urls', namespace='hijack')),#log in as another user
    path('package_monitor/', include('package_monitor.urls', namespace='package_monitor')),#monitor installed packages
    path('accounts/', include('organizations.urls')), 
    path('invitations/', include(invitation_backend().get_urls())),
    path('sentry-debug/', trigger_error),
]
    # Allow error pages to be tested
urlpatterns += [
    url(r'^403$', handler403, {'exception': Exception()}),
    url(r'^404$', handler404, {'exception': Exception()}),
    url(r'^500$', handler500),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
