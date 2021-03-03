from django.urls import path
from . import views
urlpatterns = [
    path('mpesa/payment',views.mpesa_payment, name='mpesa_payment'),
    path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
]