from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField()
    image_back = models.CharField()
    types = models.ManyToManyField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class PokemonType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'