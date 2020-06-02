from django.shortcuts import render

from pokemon.models import Pokemon, PokemonType

def pokedex(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon,
    }
    return render(request, 'pokedex.html', context)