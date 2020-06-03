from django.contrib import admin
from .models import Pokemon, PokemonType

# Register your models here.
admin.site.register(PokemonType)
admin.site.register(Pokemon)