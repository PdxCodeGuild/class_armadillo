from django.db import models
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(AbstractUser):
    phone_number = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='users', null=True)


class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField()






