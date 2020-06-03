from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Pokemon, PokemonType

# Create your views here.
def index(request):

    context = {"Pokemon": Pokemon.objects.order_by('number')}
    return render(request, 'index.html', context)


def details(request, name):
    pokemon_details = Pokemon.objects.get(name=name)
    context = {
        "pokemon_details": pokemon_details,
    }
    return render(request, "details.html", context)


