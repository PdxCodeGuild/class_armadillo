from django.db import models
import datetime
from django.conf import settings

from django.utils import timezone

# Create your models here.
class contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True,null=True)
    birthday = models.DateField(default= 'YYYY/DD/MM')
    telephone = models.CharField(max_length=15,blank=True,null=True)    
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'