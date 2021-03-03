from decouple import config
# The Mpesa environment to use
# Possible values: sandbox, production
MPESA_ENVIRONMENT = 'sandbox'
# Credentials for the daraja app
MPESA_CONSUMER_KEY =  config('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET =  config('MPESA_CONSUMER_SECRET')
#Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page
MPESA_SHORTCODE =  config('MPESA_SHORTCODE')
# Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# This only has a different value on sandbox, you do not need to set it on production
# For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page
MPESA_EXPRESS_SHORTCODE =  config('MPESA_EXPRESS_SHORTCODE')
# Type of shortcode
# Possible values:
# - paybill (For Paybill)
# - till_number (For Buy Goods Till Number)
MPESA_SHORTCODE_TYPE = 'till_number'
# Lipa na MPESA Online passkey
# Sandbox passkey is available on test credentials page
# Production passkey is sent via email once you go live

MPESA_PASSKEY =  config('MPESA_PASSKEY')