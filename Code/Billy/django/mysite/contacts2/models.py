from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    birthday = models.DateTimeField()
    phone_number = models.CharField(max_length=20)
    is_cell = models.BooleanField()
    comments = models.TextField()

    def __str__(self):
        return self.last_name + ', ' + self.first_name
