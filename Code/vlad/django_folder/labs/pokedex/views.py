from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirects


# Create your views here.

def index(request):
    context = {
        'message': 'Hello World! Pokemons'

    }
    return render(request, 'pokedex/index.html', context)
