from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json 
from .models import Pokemon, PokemonType
# Create your views here.

def index(request):
    pokemon = Pokemon.objects.order_by('name')

    context = {'pokemon': pokemon}

    return render(request, 'pokedex/index.html', context)

def detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, number=pokemon_id)
   
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon })
 
    
