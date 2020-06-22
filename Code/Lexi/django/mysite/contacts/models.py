from django.db import models
from django.utils import timezone
from phone_field import PhoneField
import datetime


# raw data
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birthday = models.DateField(default="YYYY-MM-DD")
    phone_number = PhoneField(blank=True, max_length=10)
    is_cell = models.BooleanField()
    comments = models.TextField(blank=True)

    def __str__(self):
        # last_name will be unicode strings.
        return f' last name: {self.last_name} age of humanoid: {self.age}'

class MyModel(models.Model):
    my_image = models.ImageField(upload_to='images/')