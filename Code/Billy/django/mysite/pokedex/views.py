from django.shortcuts import render
from django.http import HttpResponse

from .models import Pokemon, PokemonType

def index(request):
    
    return render(request, 'pokedex/index.html', {})
