from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
import json 
from .models import Pokemon, PokemonType
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    pokemon = Pokemon.objects.all()
    page = request.GET.get('page', 1)
    search = ''
    if request.method == 'POST':
        search = request.POST['search']
        pokemon = pokemon.filter(Q(number__icontains=search)
        | Q(name__icontains=search)
        | Q(types__name__icontains=search))

    paginator = Paginator(pokemon, 10)
    pokemon = paginator.page(page)

    context = {'pokemon': pokemon,
    'search': search
    }











    return render(request, 'pokedex/index.html', context)

def detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(number=pokemon_number)
    print(pokemon.types.all())
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon })
 
    
