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


def detail(request, pokemon_id):  # contact_id each person have a unique contact_id
    # I am searching by number
    pokemon = get_object_or_404(Pokemon, number=pokemon_id)
    # {'contact': contact}) this is giving a single contact this is why is singular because when we click the name of one of the people in the contact list it will give only that person contact details instead of everyone else
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon})


# def create_pokemon_page(request):
#     return render(request, 'pokemon/new_pokemon.html')
