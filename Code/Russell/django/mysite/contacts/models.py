from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=55)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
