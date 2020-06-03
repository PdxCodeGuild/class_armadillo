from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon, PokemonType
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    context = {
        'message': 'Gotta Catch em\' All!'
    }
    return render(request, 'pokedex/index.html', context)


