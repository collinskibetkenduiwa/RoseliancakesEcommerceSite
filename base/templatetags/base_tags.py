from django import template
from ..models import Owl_Carousel
from ..models import External_Services_Inner_Head
from ..models import External_Services_Bellow_Head
from ..models import External_Services_Head_First_Item
from ..models import TermsAndConditions
from ..models import Footer
from ..models import Footer_Social
from ..models import Checkout_Footer

register = template.Library()

@register.simple_tag
def partners():    
    
    return Owl_Carousel.objects.all()

@register.simple_tag
def footer():    
    
    return Footer.objects.all()

@register.simple_tag
def footer_social():    
    
    return Footer_Social.objects.all()

@register.simple_tag
def footer_checkout():    
    
    return Checkout_Footer.objects.all()

@register.simple_tag
def terms_and_conditions():    
    
    return TermsAndConditions.objects.all()

@register.simple_tag
def inner_head():    
    
    return External_Services_Inner_Head.objects.all()

@register.simple_tag
def bellow_head():    
    
    return External_Services_Bellow_Head.objects.all()

@register.simple_tag
def head_first_item():    
    
    return External_Services_Head_First_Item.objects.all()
