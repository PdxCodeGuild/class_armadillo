from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthday = models.DateField()
    phone_number = models.CharField(max_length=14)
    is_cell = models.BooleanField(default=True)
    comments = models.TextField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
