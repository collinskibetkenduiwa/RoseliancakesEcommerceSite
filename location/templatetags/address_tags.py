from django import template
from ..models import County
from ..models import Town

register = template.Library()

@register.simple_tag
def county():    
    return County.objects.all()

@register.simple_tag
def towns():    
    return Town.objects.all()
