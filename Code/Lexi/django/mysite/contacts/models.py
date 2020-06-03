from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birthday = models.DateField()
    phone_number = models.CharField(unique=True, blank=True, max_length=10)
    is_cell = models.BooleanField()
    comments = models.TextField()

    def __str__(self):
        # last_name will be unicode strings.
        return f' last name: {self.last_name} age of humanoid: {self.age}'

class MyModel(models.Model):
    my_image = models.ImageField(upload_to='images/')