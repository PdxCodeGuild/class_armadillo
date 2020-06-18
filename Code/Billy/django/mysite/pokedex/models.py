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
    image_front = models.URLField(max_length=200)
    image_back = models.URLField(max_length=200)
    url = models.URLField(max_length=200, blank=True, null=True)
    types = models.ManyToManyField(PokemonType, related_name='pokemons')

    def __str__(self):
        return self.name + ' ' + '(' + str(self.number) +')'
    