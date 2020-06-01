
from django.db import models
from django.utils import timezone
from phone_field import PhoneField
import datetime

# Create your models here.
class Contacts(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birth_date = models.DateField(default="YYYY-MM-DD")
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    is_cell = models.BooleanField()
    comments = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


