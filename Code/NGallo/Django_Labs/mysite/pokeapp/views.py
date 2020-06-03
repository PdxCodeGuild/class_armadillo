from django.shortcuts import render
from .models import Pokemon, PokemonType
def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'pokeapp/index.html', context)

def index(request):
    # getting all the pokemon by number
    pokemon_by_number = Pokemon.objects.order_by('number')
    context = {
        'pokemon_by_number': pokemon_by_number
    }
    return render(request,'todoapp/index.html', context)