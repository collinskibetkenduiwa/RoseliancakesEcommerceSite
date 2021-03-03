from django.contrib import admin
from .models import CheckoutPaymentRequest
        
          
class PaymentErrors(admin.ModelAdmin):
    
    list_display= ['time','phone','amount','critical','ticketed']
    readonly_fields=['time','phone','amount','critical','error',]
    list_display_links = ('time','phone','amount','critical',)
    list_filter = ['time',]
    search_fields = ['phone']
    ordering = ('-time',) 
    list_per_page = 100 
    
admin.site.register(CheckoutPaymentRequest,PaymentErrors)