from django.db import models
from ckeditor.fields import RichTextField

class CheckoutPaymentRequest(models.Model):
    time     = models.DateTimeField(auto_now=True,)
    phone    = models.CharField(max_length=50)
    amount   = models.CharField(max_length=50)
    user     = models.CharField(max_length=50,verbose_name="User agent")
    critical = models.CharField(max_length=50, verbose_name="criticality")
    error    = models.TextField()
    notes    = RichTextField(blank=True)
    seen     = models.BooleanField(default=False)#cannot be visible in admin 
    ticketed = models.BooleanField(default=False)
        
    class Meta:
        verbose_name = 'Errors during payment request'
            