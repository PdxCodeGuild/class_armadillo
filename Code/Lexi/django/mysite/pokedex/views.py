from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Pokemon, PokemonType



def index(request):
    context = {
        "Pokemon": Pokemon.objects.order_by('number')}
    
    return render(request, 'index.html', context)

def details(request, name):
    pokemon_details = Pokemon.objects.get(name=name)
    context = {
        "pokemon_details": pokemon_details,
    }
    return render(request, 'details.html', context)
