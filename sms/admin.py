from django.contrib import admin
from .models import Credits,Sent_Sms,Unsent_Sms,Starred_Sms
from sms.views import get_credit
from django.http import HttpResponseRedirect
from django.utils.html import format_html
class Credit(admin.ModelAdmin):
    change_list_template = "admin/credit_changeform.html"
    def has_add_permission(self,request):
        return False
    def has_delete_permission(self,request):
        return False

    list_display= ['date','credits']
    readonly_fields=[ 'date','credits',]
    ordering = ('-date',) 
    list_per_page = 5 
class SentSms(admin.ModelAdmin):
    def has_add_permission(self,request):
        return False
    def has_delete_permission(self,request):
        return False
    list_display= ['date','phone_number','message_id']
    readonly_fields=[ 'date','phone_number','message_id']
    ordering = ('-date',) 
    list_per_page = 100 
class StarredSms(admin.ModelAdmin):
    def has_add_permission(self,request):
        return False
    def has_delete_permission(self,request):
        return False
    actions = ["export_as_csv"]
    list_display= ['date','mobile_number','error_code','error_description']
    readonly_fields=[ 'date','mobile_number','error_code','error_description']
    list_filter = ['date','error_code','resent']
    ordering = ('-date',) 
    search_fields = ['phone_number']
    list_per_page = 100 
class UnsentSms(admin.ModelAdmin):
    def has_add_permission(self,request):
        return False
    def has_delete_permission(self,request):
        return False
    list_display= ['date','phone_number','station','resent']
    readonly_fields=[ 'date','phone_number','station',]
    list_display_links = ('date','phone_number','station','resent' )
    list_filter = ['date','station','resent']
    search_fields = ['phone_number']
    ordering = ('-date',) 
    list_per_page = 100 
    
admin.site.register(Credits,Credit)
admin.site.register(Sent_Sms,SentSms)
admin.site.register(Starred_Sms,StarredSms)
admin.site.register(Unsent_Sms,UnsentSms)