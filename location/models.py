from django.db import models

class County(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
    class Meta:
           verbose_name = 'County'

class Town(models.Model):
    County      = models.ForeignKey(County, on_delete=models.CASCADE)
    Name        = models.CharField(max_length=30)
    Postal_Code = models.CharField(max_length=12,blank=True)
    Price       = models.IntegerField(default=100)
    

    def __str__(self):
        return self.Name
    class Meta:
       verbose_name = 'Towns'