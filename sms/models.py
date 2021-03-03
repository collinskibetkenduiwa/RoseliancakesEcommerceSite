from django.db import models
class Credits(models.Model):
    date=models.DateTimeField(auto_now=True,)
    credits=models.CharField(max_length=50)
    class Meta:
            verbose_name = 'Uwazii SMS Credit'
            
class Sent_Sms(models.Model):
    date=models.DateTimeField(auto_now=False)
    phone_number=models.CharField(max_length=50,verbose_name="Phone Number")
    message_id=models.CharField(max_length=250,verbose_name="Message Id")
    
    class Meta:
            verbose_name = 'Sent sms'
            
class Starred_Sms(models.Model):
    date=models.DateTimeField(auto_now=False)
    error_code=models.CharField(max_length=50,verbose_name="Error code")
    error_description=models.CharField( max_length=50,verbose_name="Error description")
    mobile_number=models.CharField(max_length=50,verbose_name="Mobile Number")
    message_id =models.CharField(max_length=50,verbose_name="Message_Id")
    message=models.CharField(max_length=250)
    resent=models.BooleanField(default=False)
    Time_resent=models.CharField( max_length=50,verbose_name="Time resent",blank=True)            
    class Meta:
            verbose_name = 'Starred sms'

class Unsent_Sms(models.Model):
    date=models.DateTimeField(auto_now=False) 
    message= models.CharField(max_length=250)
    error =models.CharField(max_length=50)
    station = models.CharField(max_length=250)
    phone_number= models.CharField(max_length=250)
    resent=models.BooleanField(default=False)
    time_resent=models.CharField(max_length=50,verbose_name="Time resent",blank=True)
    
    class Meta:
            verbose_name = 'Unsent sms'

    