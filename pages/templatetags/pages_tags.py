from django import template
from ..models import Carousel_Home,Carousel_Home_mobile

register = template.Library()


@register.simple_tag
def homemaincarousel():    
    
    return Carousel_Home.objects.all()

@register.simple_tag
def homemobilecarousel():    
    
    return Carousel_Home_mobile.objects.all()

