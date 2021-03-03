from django.urls import path
from . import views 

urlpatterns = [
  
    path('contact',views.contact,name='contact'),
    # path('home',views.home_redirect,name='home_redirect'),
]


