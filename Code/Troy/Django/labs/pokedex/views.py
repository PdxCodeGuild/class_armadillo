from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon, PokemonType
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q



def index(request):
    pokemon = Pokemon.objects.order_by('number')
    search= ''
    pokemon = Pokemon.objects.filter(
        Q(name=name)| Q(number=number)
    )
    data = {
        'pokemon': pokemon,
        'search': search
    }
    return render(request, 'pokedex/index.html', data)

def detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'pokedex/detail.html', {'pokemon':pokemon})

# def powers(request):
