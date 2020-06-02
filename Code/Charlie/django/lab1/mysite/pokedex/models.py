from django.db import models
from django.conf import settings


class pokemon_type(models.Model):
    name = models.CharField(max_length=50)

class pokemon(models.Model):
    number = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=50)
    height = models.IntegerField(blank=True,null=True)
    weight = models.IntegerField(blank=True,null=True)
    image_font = models.CharField(max_length=50)
    image_back = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.number} {self.name}'


# Create your models here.
