from django.shortcuts import render
from .models import Pokemon, PokemonType
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

def index(request):
    pokemon = Pokemon.objects.order_by('number')
    search = ''
    if request.method == 'POST':
        search = request.POST['search']
        pokemon = pokemon.filter(Q(name__icontains=search))
    template = loader.get_template('pokedex/index.html')
    context = {
        'pokemon': pokemon,
        'search': search
    }
    return HttpResponse(template.render(context, request))


