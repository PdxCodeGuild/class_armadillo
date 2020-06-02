from django.contrib import admin

from pokemon.models import Pokemon, PokemonType

admin.site.register(Pokemon)
admin.site.register(PokemonType)
