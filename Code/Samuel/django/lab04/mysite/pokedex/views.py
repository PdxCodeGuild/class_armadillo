from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from .models import Pokemon, Type

def index(request):
    list_of_pokemon = Pokemon.objects.order_by('number')
    template = loader.get_template('pokedex/index.html')
    context = {
        'list_of_pokemon': list_of_pokemon,
    }
    return HttpResponse(template.render(context, request))

def pokemon_id(request, pokemon_id):
    single_pokemon = Pokemon.objects.filter(pk=pokemon_id).first()
    template = loader.get_template('pokedex/single.html')
    context = {
        'single_pokemon': single_pokemon,
    }
    return HttpResponse(template.render(context, request))

def pokemon_type(request):
    list_of_pokemon = Pokemon.objects.all()
    for poke in list_of_pokemon:
        print(poke)
    template = loader.get_template('pokedex/types.html')
    context = {
        'list_of_pokemon': list_of_pokemon,
    }
    return HttpResponseRedirect(reverse('pokedex:pokemon_type', args=(list_of_pokemon.id,)))
