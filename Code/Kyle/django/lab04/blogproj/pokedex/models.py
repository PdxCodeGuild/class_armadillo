from django.db import models
import json

# Create your models here.

class PokemonType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name}'

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField(PokemonType)
    
    def __str__(self):
        return f'{self.name} ({self.types})'

