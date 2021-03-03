from django import template
from ..models import Product_Shipping_And_Returns
from ..models import Product_Extra_Info

register = template.Library()

@register.simple_tag
def shipping():    
    
    return Product_Shipping_And_Returns.objects.all()

@register.simple_tag
def extra_info():    
    
    return Product_Extra_Info.objects.all()

