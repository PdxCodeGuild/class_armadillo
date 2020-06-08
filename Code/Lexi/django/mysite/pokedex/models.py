from django.db import models


# Create your models here.
class PokemonType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'
    
    # https://docs.djangoproject.com/en/3.0/ref/models/options/
    class Meta:
        ordering = ['name']

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=20)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=20)
    image_back = models.CharField(max_length=20)
    types = models.ManyToManyField('PokemonType', related_name='pokemon')
    url = models.URLField(null=True)

    def __str__(self):
        return f'{self.name} {self.number}'
        # results in; dratini 147
  
       

