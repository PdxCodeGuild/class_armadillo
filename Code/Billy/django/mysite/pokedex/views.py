from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from .models import Pokemon, PokemonType

def index(request):
    
    pokemon = Pokemon.objects.all()

    search = ''

    if request.method == 'POST':
        search = request.POST['search_poke']
        pokemon = pokemon.filter(Q(name__icontains=search)
        | Q(number__icontains=search)
        | Q(types__name__icontains=search))

    context = {
        'title': 'Pokedex',
        'pokemon': pokemon
    }
    # return render(request, 'pokedex/index.html', {})
    return render(request, 'pokedex/index.html', context)
    
