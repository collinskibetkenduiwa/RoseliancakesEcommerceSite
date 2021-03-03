from django.contrib import admin
from .models import ClearOrders

class ClearOder(admin.ModelAdmin):
    def has_add_permission(self,request):
        return False
    def has_delete_permission(self,request):
        return False
    list_display=['SystemDate','Order_no','Name','Phone','Shipping_method','Shipping_code','Date_placed','Signature','Name_other','Phone_no','Relationship',]
    list_display_links = ('SystemDate','Order_no','Name','Phone','Date_placed','Signature','Name_other','Phone_no','Relationship',)
    list_filter = ['SystemDate',]
    search_fields = ['phone','Name','Date_placed','SystemDate','Name_Other','Phone_no']
    ordering = ('-SystemDate',) 
    list_per_page = 100 
    
admin.site.register(ClearOrders,ClearOder)





    