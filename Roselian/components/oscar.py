from oscar.defaults import *
OSCAR_SHOP_NAME='Roselian'
OSCAR_HOMEPAGE='/'
OSCAR_SHOP_TAGLINE='𝖎𝖓𝖉𝖚𝖑𝖌𝖊 𝖆𝖙 𝖞𝖔𝖚𝖗 𝖈𝖔𝖓𝖛𝖎𝖓𝖎𝖊𝖓𝖈𝖊'
OSCAR_CURRENCY_FORMAT='KSh'
OSCAR_IMAGE_FOLDER='media'
OSCAR_RECENTLY_VIEWED_PRODUCTS=4
OSCAR_RECENTLY_VIEWED_COOKIE_LIFETIME= 604800 # (1 week in seconds)
OSCAR_RECENTLY_VIEWED_COOKIE_NAME='roselian_history'
OSCAR_ALLOW_ANON_CHECKOUT = True
# # pagination
OSCAR_PRODUCTS_PER_PAGE=24
OSCAR_OFFERS_PER_PAGE=12
OSCAR_REVIEWS_PER_PAGE=5
OSCAR_NOTIFICATIONS_PER_PAGE=30
OSCAR_EMAILS_PER_PAGE=50
OSCAR_ORDERS_PER_PAGE=50
OSCAR_ADDRESSES_PER_PAGE=50
OSCAR_STOCK_ALERTS_PER_PAGE=30
OSCAR_DASHBOARD_ITEMS_PER_PAGE=100
# #checkout settings
ALLOW_ANON_CHECKOUT=True #If set to False users are required to authenticate before they can checkout 
OSCAR_REQUIRED_ADDRESS_FIELDS=('first_name', 'line1','line2', 'line4','')
OSCAR_ALLOW_ANON_REVIEWS=False# If it is set to True anonymous users can create product reviews.
OSCAR_MODERATE_REVIEWS=True#If set to False a review created by a customer is immediately visible on the product page.
OSCAR_EAGER_ALERTS=True#This enables sending alert notifications/emails instantly when products get back in stock by listening to stock record update signals this might impact performance for large numbers stock record updates. Alternatively, the management command oscar_send_alerts can be used to run periodically, e.g. as a cronjob. In this case instant alerts should be disabled.
OSCAR_SEND_REGISTRATION_EMAIL=False
OSCAR_FROM_EMAIL='Admin@roseliancakes.co.ke'
OSCAR_CSV_INCLUDE_BOM=True
# # Basket settings
OSCAR_BASKET_COOKIE_LIFETIME=604800 #(1 week in seconds) The time to live for the basket cookie in seconds.
OSCAR_MAX_BASKET_QUANTITY_THRESHOLD=20#The maximum number of products that can be added to a basket at once. Set to None to disable the basket threshold limitation.
OSCAR_BASKET_COOKIE_OPEN='roselian_open_basket'
# Currency settings
OSCAR_DEFAULT_CURRENCY= 'Ksh'
EMAIL_BACKEND = 'post_office.EmailBackend'
OSCAR_DELETE_IMAGE_FILES=True
OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'phone_number',)
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
# This dict defines the new order statuses than an order can move to
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed','shipping','pickup','Cancelled',),
    'Being processed': ('Shipped','Pickup','Complete', 'Cancelled',),
    'Shipped': ('Pickup','Complete',),
    'Pickup': ('Complete',),
    'Complete': (),
}
# This dict defines the line statuses that will be set when an order's status
OSCAR_ORDER_STATUS_CASCADE = {
    'Being processed': 'Being processed',
    'Cancelled': 'Cancelled',
    'Complete': 'Shipped',
    'Arrived': 'Pickup',
    'Pickup': 'Complete',
    'Bounced': 'Bounced',
}
OSCAR_USE_LESS = False
OSCAR_STATIC_BASE_URL='/static/'
OSCAR_DASHBOARD_NAVIGATION[5]['children'] += [     
    {
        'label': 'Content blocks',
        'url_name': 'oscar_promotions_dashboard:promotion-list',
    },
    {
        'label': 'Content blocks by page',
        'url_name': 'oscar_promotions_dashboard:promotion-list-by-page',
    },
]
OSCAR_PROMOTION_FOLDER="promotions"