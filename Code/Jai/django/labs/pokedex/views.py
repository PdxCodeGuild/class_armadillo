from django.shortcuts import render
from django.http import HttpResponse
import json 
from .models import Pokemon, PokemonType
# Create your views here.

def index(request):
    pokemons = Pokemon.objects.all()

    context = {'pokemons': pokemons}

    return render(request, 'pokedex/index.html', context)

def detail(request, pokemon_number):
    pokemon = Pokemon.objects.get(number=pokemon_number)
    
    print(pokemon.types.all())
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon })


   

               
    
               
               
               
               
               
              
 