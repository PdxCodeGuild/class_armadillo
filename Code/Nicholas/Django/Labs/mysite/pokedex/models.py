from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    number = models.IntegerField(max_length=3)
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField()
    image_back = models.Charfield()
    types = models.ManyToManyField(PokemonType, related_name='')

    def __str__(self):
        return self.image_front + ' ' + self.name