
from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['name']

# Create your models here.                                     
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField(PokemonType, related_name='pokemon')

    def __str__(self):
        return f'{self.name} {self.number}'

    class Meta:
        ordering = ['name']