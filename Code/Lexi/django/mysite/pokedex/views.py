from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonType
from django.urls import reverse
from django.http import HttpResponse




def index(request):
    context = {
        "Pokemon": Pokemon.objects.order_by('number')}
    
    return render(request, 'pokedex/index.html', context)

def detail(request, pokedex_id):
    pokemon = get_object_or_404(Pokemon, pk=pokedex_id)
    context = {
        "pokemon_detail": pokemon_detail,
    }
    return render(request, 'detail.html', context)
