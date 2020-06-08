from django.db import models
import json



# PokemonType should have the following fields:
class PokemonType(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name

    





class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    numbers = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.URLField(max_length=200)
    image_back = models.URLField(max_length=200)
    types = models.CharField(max_length=20)
    

    def __str__(self):
        return f'{self.name} {self.image_front} {self.image_back}'
        #     "name": "bulbasaur",
        #     "height": 7,
        #     "weight": 69,
        #     "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        #     "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
        #     "types": [
        #         "poison",
        #         "grass"
        #     ],
        #     "url": "https://pokemon.fandom.com/wiki/bulbasaur"
        # },



# Pokemon should have the following fields:

# number (IntegerField)
# name (CharField)
# height (IntegerField)
# weight (IntegerField)
# image_front (CharField)
# image_back (CharField)
# types (MantToManyField with PokemonType)

