from django.shortcuts import render, get_object_or_404, reverse
from .models import Pokemon
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
def index(request):
    context = {
        'message': 'Hello Pokemon World'
    }
    return render(request, 'pokedex/index.html', context)

def index(request):
    pokemon = Pokemon.objects.order_by('number')
    context = {
        'title': 'Pokedex',
        'pokemon': pokemon
    }
    return render(request, 'pokedex/index.html', context)
