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
    types = []  # make a list of just the types
    for type in pokemon.types.all():
        print(type)
        types.append(type.name)

    # {'contact': contact}) this is giving a single contact this is why is singular because when we click the name of one of the people in the contact list it will give only that person contact details instead of everyone else
    # to get a list of the types to turn the query set of the types into a list: list(pokemon.types.all())
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon, 'types': ', '.join(types)})


# on line 22 create an empty list then loop each pokemon.types.all
# then append the name of each type to the list
# this will give me the name
# in the template detail I can use the join method
# Using list comprehension way to do it below:
# #types = ', '.join([p_type.name for p_type in pokemon.types.all()])


# # def create_pokemon_page(request):
#     return render(request, 'pokemon/new_pokemon.html')
