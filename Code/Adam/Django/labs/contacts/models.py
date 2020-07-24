from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthday = models.DateField()
    phone_number = models.CharField(max_length=50)
    is_cell = models.BooleanField()
    comments = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name