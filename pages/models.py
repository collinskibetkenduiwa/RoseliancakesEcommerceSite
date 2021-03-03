from django.db import models
from ckeditor.fields import RichTextField

class Carousel_Home(models.Model):
    Name            = models.CharField(max_length=64,blank=True,)
    Description     = models.TextField(blank=True,verbose_name="What is the use of this carousel")
    Title           = models.CharField( blank=True,max_length=128,)
    Content         = RichTextField(blank=True)
    Url             = models.URLField(blank=True,)
    Button_Title    = models.CharField(blank=True,max_length=50)
    Image           = models.ImageField(blank=True,upload_to='media/pages/carousel/',)
    
    class Meta:
        verbose_name = u'Home page main carousel'
        
class Carousel_Home_mobile(models.Model):
    Name            = models.CharField(max_length=64,blank=True,)
    Description     = models.TextField(blank=True,verbose_name="What is the use of this carousel")
    Title           = models.CharField( blank=True,max_length=128,)
    Content         = RichTextField(blank=True)
    Url             = models.URLField(blank=True,)
    Button_Title    = models.CharField(blank=True,max_length=50)
    Image           = models.ImageField(blank=True,upload_to='media/pages/mobile/carousel/',)
    class Meta:
        verbose_name = u'Home mobile main carousel'
        
    
class User_Contacts(models.Model):
    Name     = models.CharField( max_length=150)
    Email    = models.CharField(max_length=150)
    Phone    = models.CharField( max_length=50)
    Subject  = models.CharField( max_length=250,blank=True)
    Message  = models.TextField()
    Time     = models.TimeField(auto_now_add=True)
    Resolved = models.BooleanField(default=False)
    Notes    = models.TextField(blank=True)
    
    class Meta:
        verbose_name = u'User queries from contact page' 