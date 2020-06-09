from django.shortcuts import render
from django.http import HttpResponse

from .models import Pokemon, PokemonType

def index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokedex/index.html', {'pokemon': pokemon})

