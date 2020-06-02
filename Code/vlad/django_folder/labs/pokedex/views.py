from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def index(request):
    pokemon = Pokemon.object.order_by('name')
    context = {
        'pokemon': pokemon

    }
    return render(request, 'pokedex/index.html', context)
