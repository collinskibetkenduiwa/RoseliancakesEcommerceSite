from django.contrib import admin
from .models import Town, County

class Counties(admin.ModelAdmin):
    list_display= ['Name',]
    list_display_links = ( 'Name', )
    # list_editable=['Name',]
    search_fields = ['Name',]
    ordering = ('id',) 
    list_per_page = 100 

class Towns(admin.ModelAdmin):
    list_display= ['County','Name','Postal_Code','Price',]
    list_display_links = ( 'County','Name','Postal_Code','Price', )
    # list_editable = ['County','Name','Postal_Code','Price', ]
    list_filter = ['County','Price',]
    search_fields = ['Name','Postal_Code']
    ordering = ('id',) 
    list_per_page = 100 

admin.site.register(County,Counties)
admin.site.register(Town,Towns)
