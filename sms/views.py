from django.conf import settings
import requests
from django.http import HttpResponsePermanentRedirect
from .models import Credits

def get_credit(request):
    parameters = {
    'ApiKey':getattr(settings,"UwaziiApiKey",'dqtbG8VS++yUYVWst5vQy/7DRSzizWNqhk3HQjtR5FI='),
    'ClientId':getattr(settings,"UwaziiClientId",'84f16b13-1111-4ade-88c9-242bf0031ebc')
    }
    if request.method=="POST":
        previous_url = request.META.get('HTTP_REFERER')
        response = requests.get("https://api.uwaziimobile.com/api/v2/Balance?", params=parameters)
        response=response.json()
        data=response.get('Data')[0]
        credits=data.get("Credits")
        new_credit=Credits(credits=credits)
        new_credit.save()
        return HttpResponsePermanentRedirect(previous_url)
    else:
        response = requests.get("https://api.uwaziimobile.com/api/v2/Balance?", params=parameters)
        response=response.json()
        data=response.get('Data')[0]
        credits=data.get("Credits")
        new_credit=Credits(credits=credits)
        new_credit.save()
        return "ok"
        
def send_sms(phone_number,message):
    parameters = {
    'ApiKey':getattr(settings,"UwaziiApiKey",'dqtbG8VS++yUYVWst5vQy/7DRSzizWNqhk3HQjtR5FI='),
    'ClientId':getattr(settings,"UwaziiClientId",'84f16b13-1111-4ade-88c9-242bf0031ebc'),
    'SenderId':"Uwazii",
    'Message':message,
    'MobileNumbers':phone_number,
    }
    response = requests.get("https://api.uwaziimobile.com//api/v2/SendSMS?", params=parameters)
    
