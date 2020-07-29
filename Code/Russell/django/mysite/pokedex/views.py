from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from .models import Pokemon, PokemonType

def index(request):
    search = ''
    pokemon = Pokemon.objects.all()

    

    if request.method == 'POST':
        search = request.POST['search_pokemon']
        pokemon = pokemon.filter(Q(name__icontains=search)
        #OR (|) Combines two QuerySets using the SQL OR operator.
        | Q(number__icontains=search)
        | Q(types__name__icontains=search))

    context = {
        
        'pokemon': pokemon
    }
   
    return render(request, 'pokedex/index.html', context)
    
