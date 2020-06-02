from django.db import models
'''
# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField(pokemontype)

    def __str__return(self):
        return self.name + ' - ' + slef.ty

#class PokemonType(models.Model):
   '''