from django.db import models

class PokemonType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=500)
    image_back = models.CharField(max_length=500)
    types = models.ManyToManyField(PokemonType, related_name='pokemon_set')

    def __str__(self):
        return str(self.number) + ') ' + self.name