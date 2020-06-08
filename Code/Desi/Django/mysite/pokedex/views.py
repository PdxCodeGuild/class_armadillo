from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon,PokemonType


def index(request):

    poke = Pokemon.objects.all()

    context = {'poke': poke}

    return render(request, 'index.html', context)

def detail(request, poke):
    pokemon = Pokemon.objects.get(pk=poke)
    return render(request, 'pokedex/detail.html', {'poke': poke})


    # return HttpResponse('ok')

    
