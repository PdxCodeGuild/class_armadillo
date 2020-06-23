from django.shortcuts import render
from django.http import HttpResponse

from .models import Pokemon, PokemonType

def index(request):
    
    pokemon = Pokemon.objects.all()
    context = {
        'title': 'Pokedex',
        'pokemon': pokemon
    }
    # return render(request, 'pokedex/index.html', {})
    return render(request, 'pokedex/index.html', context)
    
