from django.db import models
from django.conf import settings
# Create your models here.
class Orders(models.Model):
    name = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=10)
    alt_number = models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=800)
    landmark = models.CharField(max_length=300)
    ordered = models.FileField(upload_to='Orders/ordered')
    ordered_date = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.phonenumber

 