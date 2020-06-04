from django.shortcuts import render
from .models import Pokemon, PokemonType
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    pokemon = Pokemon.objects.order_by('number')
    template = loader.get_template('pokedex/index.html')
    context = {
        'pokemon': pokemon,
    }
    return HttpResponse(template.render(context, request))


