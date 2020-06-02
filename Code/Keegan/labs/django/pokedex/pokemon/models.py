from django.db import models

class PokemonType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'Type name: {self.name}'

class Pokemon(models.Model):
    name        = models.CharField(max_length=100)
    number      = models.IntegerField()
    height      = models.IntegerField()
    weight      = models.IntegerField()
    image_front = models.URLField(max_length=300)
    image_back  = models.URLField(max_length=300)
    url         = models.URLField(max_length=300)
    types       = models.ManyToManyField(PokemonType, related_name="pokemon")

    def __str__(self):
        return f'#{self.number}: {self.name}'
