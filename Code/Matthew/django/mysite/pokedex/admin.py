from django.contrib import admin

from pokedex.models import Pokemon, PokemonType

admin.site.register(Pokemon)
admin.site.register(PokemonType)
