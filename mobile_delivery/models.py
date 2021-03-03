from django.db import models

class ClearOrders(models.Model):
    SystemDate=models.DateTimeField(auto_now=True)
    Order_no=models.CharField( max_length=50,verbose_name="oder number")
    Name=models.CharField( max_length=150)
    Phone=models.CharField(max_length=50)
    Shipping_method = models.CharField( max_length=50,verbose_name="Shipping method")
    Shipping_code = models.CharField( max_length=50,verbose_name="shipping code")
    Date_placed =models.CharField( max_length=50,verbose_name="date_placed")
    Status=models.CharField( max_length=50)
    Signature = models.ImageField(blank=True, upload_to='media/mobile/delivery/signatures')
    Name_other=models.CharField(blank=True, max_length=150,verbose_name="Name of secondary picker")
    Phone_no=models.CharField(blank=True,max_length=50,verbose_name="secondary picker phone")
    Relationship=models.CharField(blank=True, max_length=50,verbose_name="Relationship to the owner")
    
    class Meta:
        verbose_name = 'Successful cleared orders'
    
    