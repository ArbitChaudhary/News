from django.db import models

# Create your models here.
class logoManager(models.Model):
    logo = models.ImageField(upload_to='img/')

    class Meta:
        verbose_name_plural = "Logo Manager"
    
    def __str__(self):
        return str(self.logo)

class adsManager(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='img/')

    class Meta:
        verbose_name_plural = "Ads Manager"
    
    def __str__(self):
        return str(self.name)