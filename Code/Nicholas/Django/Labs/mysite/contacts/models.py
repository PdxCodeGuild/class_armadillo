import datetime
from django import forms
from django.db import models
from django.utils import timezone

class Contacts(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birthday = models.DateField()
    phone_number = models.CharField(max_length=20)
    is_cell = forms.BooleanField() 
    comments = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
