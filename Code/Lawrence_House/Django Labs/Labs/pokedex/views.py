from django.shortcuts import render, get_object_or_404, reverse
from .models import Pokemon
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    pokemans = Pokemon.objects.order_by('number')
    context = {
        'title': 'Pokedex!',
        'pokemon': pokemans
    }
    return render(request, 'pokedex/index.html', context)