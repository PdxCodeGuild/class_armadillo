from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Pokemon, PokemonType
=======
from.models import pokedex

admin.site.register(pokedex)
>>>>>>> 4587d3b71cfb2a129eb87b7a67818aeae28a35e4

admin.site.register(Pokemon)
admin.site.register(PokemonType)