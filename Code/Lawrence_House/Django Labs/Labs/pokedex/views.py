from django.shortcuts import render, get_object_or_404, reverse
from .models import Pokemon
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    pokemans = Pokemon.objects.all()
    context = {
        'title': 'Pokedex!',
        'pokemons': pokemans,
    }
    return render(request, 'pokedex/index.html', context)

# def detail(request):
#     pass