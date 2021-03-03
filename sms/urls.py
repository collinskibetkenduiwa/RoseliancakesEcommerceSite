from django.conf.urls import url
import django_twilio
from . import views

urlpatterns = [
     url('checkcredit', views.get_credit),
]