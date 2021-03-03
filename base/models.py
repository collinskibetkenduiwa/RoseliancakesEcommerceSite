from django.db import models
from ckeditor.fields import RichTextField

class External_Services_Inner_Head(models.Model):
    Name    = models.CharField( max_length=50)
    Content = models.CharField(max_length=750,verbose_name="content inside  head")
    
    class Meta:
        verbose_name = u'External services above head'

class External_Services_Head_First_Item(models.Model):
    Name    = models.CharField( max_length=50)
    Content = models.CharField(max_length=750,verbose_name="content first items in head")
    
    class Meta:
        verbose_name = u'External services  head first item'
            
class External_Services_Bellow_Head(models.Model):
    Name    = models.CharField( max_length=50)
    Content = models.CharField(max_length=750,verbose_name="content bellow head")
    class Meta:
       verbose_name = u'External services bellow head'
    
class TermsAndConditions(models.Model):
      ######################################
    #making table ony have one record
    def save(self,*args, **kwargs):
        if not self.pk and TermsAndConditions.objects.exists():
            TermsAndConditions.objects.all().delete()
        return super(TermsAndConditions,self).save(*args, **kwargs)
    #####################################
    Content=RichTextField()
    
    class Meta:
        verbose_name = u'User Terms And Conditions'
        
class Owl_Carousel(models.Model):
    Name = models.CharField( blank=True,max_length=50)
    Logo = models.ImageField( upload_to="media/base", verbose_name="image logo for partners size is 82x41")
    Link = models.CharField(blank=True, max_length=50)
    
    class Meta:
        verbose_name = u'Partner Logo'
        verbose_name_plural = u'Partners Logos'
    
class Footer(models.Model):
     ######################################
    #making table ony have one record
    def save(self,*args, **kwargs):
        if not self.pk and Footer.objects.exists():
            Footer.objects.all().delete()
        return super(Footer,self).save(*args, **kwargs)
    #####################################
    Content         = RichTextField(verbose_name="Descriptive content bellow the logo")
    Phone           = models.CharField( max_length=50)
    Email           = models.CharField(blank=True, max_length=50)
    Quick_Links     = RichTextField(blank=True,verbose_name="Quick links eg contact us in a list form")
    Legal           = RichTextField(blank=True,verbose_name="Legal links eg Privacy policy  in a list form")
    Brand_One       = models.ImageField(upload_to="media/base/footer") 
    Link_One        = models.CharField(max_length=50)
    Brand_Two       = models.ImageField(upload_to="media/base/footer")
    Link_Two        = models.CharField(max_length=50)
    Brand_Three     = models.ImageField(upload_to="media/base/footer") 
    Link_Three      = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = u'Main Footer'

class Footer_Social(models.Model):
    Twitter    = models.CharField(blank=True,verbose_name="Twitter account link", max_length=50)
    Pinterest  = models.CharField(blank=True,verbose_name="Pintrest account link", max_length=50)
    Facebook   = models.CharField(blank=True,verbose_name="Facebook account link", max_length=50)
    Youtube    = models.CharField(blank=True,verbose_name="Youtube account link", max_length=50)
    Instagram  = models.CharField(blank=True,verbose_name="Instagram account link", max_length=50)
    
    class Meta:
        verbose_name=u'Social media links at the footer'        
        
class Checkout_Footer(models.Model):
    Main_Content      = RichTextField(verbose_name="Main content")
    Secondary_Content = RichTextField(verbose_name="Secondary content in the second column")
    Tertial_Content   = RichTextField(verbose_name="Tertial content in the third column")
    
    class Meta:
        verbose_name = u'Checkout footer'
    
    
class Product_Shipping_And_Returns(models.Model):
    ######################################
    #making table ony have one record
    def save(self,*args, **kwargs):
        if not self.pk and Product_Shipping_And_Returns.objects.exists():
            Product_Shipping_And_Returns.objects.all().delete()
        return super(Product_Shipping_And_Returns,self).save(*args, **kwargs)
    Content = RichTextField()
    
        
    class Meta:
        verbose_name = u'Product shipping and returns'
        
class Product_Extra_Info(models.Model):
    ######################################
    #making table ony have one record
    def save(self,*args, **kwargs):
        if not self.pk and Product_Extra_Info.objects.exists():
            Product_Extra_Info.objects.all().delete()
        return super(Product_Extra_Info,self).save(*args, **kwargs)
    ######################################
    Content = RichTextField()
        
    class Meta:
        verbose_name = u'Product extra information'   
        

