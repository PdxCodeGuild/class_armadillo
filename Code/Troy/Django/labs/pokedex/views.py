from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon, PokemonType
from django.urls import reverse
from django.http import HttpResponseRedirect



def index(request):
    pokemon = Pokemon.objects.order_by('number')
    data = {
        'pokemon': pokemon
    }
    return render(request, 'pokedex/index.html', data)

def detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokedex, pk=pokemon_id)

# def pokemon_data(request):
#     number = request.POST['number']
#     name = request.POST['name']
#     height = request.POST['height']
#     weight = request.POST['weight']
#     image_front = request.POST['image_front']
#     image_back = request.POST['image_back']
#     types = request.POST['types']
#     pokemon_data = (number=number,
#         name=name,
#         height=height,
#         weight=weight,
#         image_front=image_front,
#         image_back= image_back,
#         types=types)
#     pokemon_data.save()

#     return HttpResponseRedirect(reverse('pokedex:detail', args=(pokemon.id)))