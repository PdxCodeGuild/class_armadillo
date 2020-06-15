from django.shortcuts import render
from django.http import HttpResponse

from .models import Pokemon, PokemonType

def index(request):
    pokemon = Pokemon.objects.all()
    context = {
        'title': 'Pokemon Index',
        'pokemon': pokemon
    }
    return render(request, 'pokeapp/index.html', context)
