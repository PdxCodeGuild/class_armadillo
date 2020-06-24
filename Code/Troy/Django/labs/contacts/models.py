
from django.db import models
from django.utils import timezone
from phone_field import PhoneField
import datetime

# Create your models here.
class Contacts(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birth_date = models.DateField()
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    is_cell = models.BooleanField()
    comments = models.TextField(blank=True)

    def format_bday (self):
        return self.birth_date.strftime('%Y-%m-%d')

    def __str__(self):
        return self.last_name + ', ' + self.first_name


