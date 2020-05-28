from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    birthday = models.DateField()
    phone_number = models.CharField(max_length=30)
    is_cell = models.BooleanField()
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

