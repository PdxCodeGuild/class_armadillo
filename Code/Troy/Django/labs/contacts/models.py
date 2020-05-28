
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Contacts(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birthday = models.DateField()
    phone_number = models.CharField(max_length=10)
    is_cell = models.BooleanField()
    comment = models.TextField()

    def __str__(self):
        return self.Contacts


