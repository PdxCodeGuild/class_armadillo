from django.shortcuts import render
from django.http import HttpResponse

from .models import Pokemon, PokemonType

def index(request):
    pokemon = Pokemon.objects.all()
    context = {
        'title': 'Pokemon Index',
        'pokemon': pokemon
    }
    return render(request, 'pokeapp/index.html', context)

def detail(request):
    found_poke = request.POST['pokemon_name']
    print(request.POST['pokemon_name'])
    poke_detail = Pokemon.objects.get(name=found_poke)
    print(poke_detail)
    context = {
        'pokemon': poke_detail
    }
    return render(request, 'pokeapp/detail.html', context)
    # return HttpResponse('ok')