from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon, PokemonType



def index(request):

    pokemon = Pokemon.objects.order_by('number')

    context = {
        'pokemon': pokemon
    }
    return render(request, 'pokemon/index.html', context)

