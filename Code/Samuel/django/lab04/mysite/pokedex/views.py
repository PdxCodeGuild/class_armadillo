from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import Pokemon, Type
import string
def index(request):
    list_of_pokemon=Pokemon.objects.order_by('number')
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
    list_of_pokemon = Pokemon.objects.filter(Q(name__icontains=request.POST['search']) | Q(types__name__icontains=request.POST['search'].lower()))
    template = loader.get_template('pokedex/types.html')
    context = {
        'list_of_pokemon': list_of_pokemon,
        'query': request.POST['search']
    }
    return HttpResponse(template.render(context, request))
