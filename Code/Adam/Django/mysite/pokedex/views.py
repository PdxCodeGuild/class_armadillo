from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon, PokemonType
from django.urls import reverse


def index(request):
    context = {
        'Pokemon': Pokemon.objects.order_by('number')
    }
    return render(request, 'pokedex/index.html', context)
