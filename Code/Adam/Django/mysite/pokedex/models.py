from django.db import models


class Pokemon(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField


class PokemonType(models.Model):
    name = models.CharField(max_length=100)

