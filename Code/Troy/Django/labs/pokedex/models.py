
from django.db import models



class PokemonType(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pokemon(models.Model):

    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.ImageField(upload_to='admin/')
    image_back = models.ImageField()
    types = models.ManyToManyField(PokemonType, related_name='pokemon')
    
    def __str__(self):
        return self.name 
    def __int__(self):
        return self.number

   
