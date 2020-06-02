from django.shortcuts import render

from pokemon.models import Pokemon, PokemonType

def pokedex(request):
    pokemon = Pokemon.objects.last()
    types = ','.join([typ.name for typ in pokemon.types.all()])

    context = {
        'pokemon': pokemon,
        'types': types,
    }
    return render(request, 'pokedex.html', context)