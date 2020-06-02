from django.db import models

class PokemonType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=30)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)
    types = models.ManyToManyField(PokemonType)

    def __str__(self):
        return self.name
    
