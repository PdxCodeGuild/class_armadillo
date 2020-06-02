from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Pokemon, PokemonType


# Create your views here.

def index(request):
    # this is the name of my app Pokemon
    pokemon = Pokemon.objects.order_by('name')
    context = {
        'pokemon': pokemon

    }
    return render(request, 'pokedex/index.html', context)
