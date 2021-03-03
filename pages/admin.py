from django.contrib import admin
from django.contrib.admin import site
from django.contrib.admin import AdminSite
from base.models import External_Services_Inner_Head
from base.models import External_Services_Bellow_Head
from base.models import External_Services_Head_First_Item
from base.models import TermsAndConditions
from base.models import Owl_Carousel
from base.models import Footer
from base.models import Footer_Social
from base.models import Checkout_Footer
from base.models import Product_Shipping_And_Returns
from base.models import Product_Extra_Info
# pages
from .models import Carousel_Home,Carousel_Home_mobile
from .models import User_Contacts
#Admin customization
AdminSite.site_header='Roselian cakes Administration'
AdminSite.site_title = "Roselian cakes Admin"
AdminSite.index_title = "Welcome to Roselian cakes administrative page"

 
class InnerHead(admin.ModelAdmin):
    list_display= ['Name',]
    list_filter = ('Name',)
    search_fields = ['Name',]
    ordering = ('id',) 
    list_per_page = 20 
    
class BellowHead(admin.ModelAdmin):
    list_display= ['Name',]
    list_filter = ('Name',)
    search_fields = ['Name',]
    ordering = ('id',) 
    list_per_page = 20 
    
class FirstItemHead(admin.ModelAdmin):
    list_display= ['Name',]
    list_filter = ('Name',)
    search_fields = ['Name',]
    ordering = ('id',) 
    list_per_page = 20         

class OwlCarousel(admin.ModelAdmin):
    list_display= ['Name','Link']
    list_filter = ('Name',)
    search_fields = ['Name',]
    ordering = ('id',) 
    list_per_page = 20 
     
class User_Contact(admin.ModelAdmin):
    list_display= ['Name','Email','Phone','Subject','Resolved']
    list_filter = ('Resolved','Time')
    search_fields = ['Name','Phone']
    ordering = ('id',) 
    list_per_page = 20  
     
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Url',]
    
               
admin.site.register(External_Services_Inner_Head,InnerHead)
admin.site.register(External_Services_Bellow_Head,BellowHead)
admin.site.register(External_Services_Head_First_Item,FirstItemHead)
admin.site.register(TermsAndConditions)
admin.site.register(Owl_Carousel,OwlCarousel)
admin.site.register(Footer)
admin.site.register(Footer_Social)
admin.site.register(Checkout_Footer,)

admin.site.register(Carousel_Home_mobile,CarouselAdmin)
admin.site.register(Product_Shipping_And_Returns)
admin.site.register(Product_Extra_Info)
admin.site.register(User_Contacts,User_Contact)
admin.site.register(Carousel_Home, CarouselAdmin)



