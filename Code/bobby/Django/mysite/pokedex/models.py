from django.db import models

# Create your models here.


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Meta:
    ordering = ['name']

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=50)
    image_back = models.CharField(max_length=50)
    types = models.ManyToManyField(PokemonType)

    def __str__(self):
        return str(self.number) + '' + self.name
