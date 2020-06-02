from django.shortcuts import render
from .models import pokemon
from django.http import HttpResponse
import json
import requests

path = 'pokemon.json'

def index(request, path):
    with open(path, 'r') as file:
        text = file.read()
    pokemon = json.loads(text)
    pokemon = pokemon['pokemon']
    return render(request, 'pokedex/pokemon.json')
# Create your views here.
