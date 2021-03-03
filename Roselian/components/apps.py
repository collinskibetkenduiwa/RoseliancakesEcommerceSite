
INSTALLED_APPS = [
    'jet',#admin page
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
        # oscar
    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    'apps.checkout.apps.CheckoutConfig',
    'address.apps.AddressConfig',
    'shipping.apps.ShippingConfig',
    'oscar.apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',
    'oscar_promotions.apps.PromotionsConfig',
    'oscar_promotions.dashboard.apps.PromotionsDashboardConfig',
    # # 3rd-party oscar.apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'easy_thumbnails',
    'django_tables2',
    # ###############################
    'rest_framework',
    'oscarapi',
    'pwa', # progressive web app
    'django_extensions',
    'django_otp',#otp
    'django_otp.plugins.otp_totp',#otp
    #  "django_rq",#scheduling jobs
    # "django_rq_jobs",#scheduling jobs
    'dbbackup',  # django-dbbackup
    'admin_honeypot',#fake admin  form
    'newsletter',#collect email subscriptions
    'django.contrib.humanize',  # Required for elapsed time formatting
    'markdown_deux',  # Required for Knowledgebase item formatting
    'bootstrapform', # Required for nicer formatting of forms with the default templates
    'helpdesk',  # issue management
    'django_prometheus',#metrics
    'django.contrib.admindocs',#auto generate docs in admin 
    'django.contrib.gis.geoip2',
    'robots',#robot for site engines
    'djangobower',#Javascript Library
    'markup_deprecated',
    "post_office",
    'smuggler',
    'django_user_agents',#browser identification and render different content
    'ckeditor',# rich text editor
    'hijack_admin',#hijack admin
    'package_monitor',#monitor changes in installed packages
    'organizations',#account permissions management
    #local app 
    'base',
    'core',
    'mpesa',
    'pages',
    'simple_pages',
    'sms',
    'location',
    'compressor',
    'django_daraja',
    'logging_',
    'mobile_delivery',
]
    
