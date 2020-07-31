from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=50)
    is_cell = models.BooleanField()
    comments = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def age(self):
        return timezone.now().year - self.birthday.year