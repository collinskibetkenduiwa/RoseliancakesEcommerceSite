from decouple import config

########################django-Jet############################################
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
####################################helpdesk###########################
HELPDESK_DEFAULT_SETTINGS = {
        'use_email_as_submitter': True,
        'email_on_ticket_assign': True,
        'email_on_ticket_change': True,
        'login_view_ticketlist': True,
        'tickets_per_page': 25
        }
HELPDESK_REDIRECT_TO_LOGIN_BY_DEFAULT = True
HELPDESK_FOLLOWUP_MOD = True
HELPDESK_AUTO_SUBSCRIBE_ON_TICKET_RESPONSE = True
HELPDESK_VIEW_A_TICKET_PUBLIC = False
HELPDESK_ANON_ACCESS_RAISES_404 =True
HELPDESK_SUBMIT_A_TICKET_PUBLIC = False
HELPDESK_SHOW_DELETE_BUTTON_SUPERUSER_FOLLOW_UP = True
HELPDESK_ENABLE_PER_QUEUE_STAFF_PERMISSION = True
############################################
TWILIO_ACCOUNT_SID ='AC430a4388834881a0a1ad5af00196917c'
TWILIO_AUTH_TOKEN ='8eab227a2d4dcc6527d68b29f9d33159'
TWILIO_PHONE_NUMBER= '+19728534102'
DJANGO_TWILIO_FORGERY_PROTECTION = False
DJANGO_TWILIO_BLACKLIST_CHECK = True
TWILIO_DEFAULT_CALLERID = 'Roselian cakes'
###################################################################################
#newsletter
# NEWSLETTER_CONFIRM_EMAIL = False
NEWSLETTER_CONFIRM_EMAIL_SUBSCRIBE=True
NEWSLETTER_CONFIRM_EMAIL_UNSUBSCRIBE=True
NEWSLETTER_CONFIRM_EMAIL_UPDATE= True 
# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1
HELPDESK_ENABLE_PER_QUEUE_STAFF_PERMISSION = True
# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60
# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100
#####################################################
#post-office
POST_OFFICE = {
    'DEFAULT_PRIORITY' : 'now'
}
# EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX')
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
#################################################################
#prometheus
# ROOT_URLCONF = "graphite.urls_prometheus_wrapper"
################################################################
#admin stats
ADMIN_CHARTS_NVD3_JS_PATH = 'bow/nvd3/build/nv.d3.js'
ADMIN_CHARTS_NVD3_CSS_PATH = 'bow/nvd3/build/nv.d3.css'
ADMIN_CHARTS_D3_JS_PATH = 'bow/d3/d3.j'
# Specifie path to components root (you need to use absolute path)
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
BOWER_INSTALLED_APPS = (
    'd3#3.3.13',
    'nvd3#1.7.1',
)
SMUGGLER_FIXTURE_DIR="backup/data"
CKEDITOR_UPLOAD_PATH = 'media/content/ckeditor/'
########################hijack admin###########################
HIJACK_ALLOW_GET_REQUESTS = True
###########Progressive Web App################################
PWA_APP_NAME = 'Roselian Cakes' 
PWA_APP_DESCRIPTION = "An E-commerce for selling cakes and buying cakes"
PWA_APP_THEME_COLOR = 'pink' 
PWA_APP_BACKGROUND_COLOR = 'white' 
PWA_APP_DISPLAY = 'standalone' 
PWA_APP_SCOPE = '/' 
PWA_APP_ORIENTATION = 'any' 
PWA_APP_START_URL = '/home' 
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [ { 'src': '/static/App/icons/roselian.ico', 'sizes': '16x16' } ] 
PWA_APP_ICONS_APPLE = [ { 'src': '/static/App/icons/roselian.ico', 'sizes': '16x16' } ] 
PWA_APP_SPLASH_SCREEN = [ { 'src': '/static/App/splash/splash.jpg', 'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)' } ]
PWA_APP_DIR = 'roseliancakes' 
PWA_APP_LANG = 'en-US'
PWA_APP_DEBUG_MODE = True #to enable or disable the the console.log on browser.
##############################User tracking ###########################
# TRACK_AJAX_REQUESTS = True
# TRACK_ANONYMOUS_USERS = True
# TRACK_SUPERUSERS = False
# TRACK_PAGEVIEWS = True
# TRACK_IGNORE_URLS =['admin/']
# TRACK_IGNORE_STATUS_CODES = [400, 404, 403, 405, 410, 500]
# TRACK_REFERER =True
# TRACK_QUERY_STRING =True
DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/var/backups'}
##############################packages monitoring###########################################
PACKAGE_MONITOR_REQUIREMENTS_FILE = os.path.join(BASE_DIR, 'requirements.txt')
# compression enabled
COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]
# sms uwazii mobile
UwaziiApiKey=config('UwaziiKey')
UwaziiClientId=config('UwaziiId')