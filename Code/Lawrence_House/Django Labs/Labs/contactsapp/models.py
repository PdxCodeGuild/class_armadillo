from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=200)
    is_cell = models.BooleanField()
    comments = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' # Sets up shortcut to firstname lastname pattern