from django.db import models


# Create your models here.
class PokemonType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField(max_length=4)
    name = models.CharField(max_length=20)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=20)
    image_back = models.CharField(max_length=20)
    types = models.ManyToManyField('PokemonType', related_name='pokemon')

    def __str__(self):
        return self.image_front
    def __str__(self):
        return self.name 
    def __int__(self):
        return self.number