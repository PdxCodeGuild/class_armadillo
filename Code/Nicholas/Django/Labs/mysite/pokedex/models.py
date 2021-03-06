from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField(PokemonType, related_name="pokemon")

    def __str__(self):
        return str(self.number)+ '.' + ' ' + self.name