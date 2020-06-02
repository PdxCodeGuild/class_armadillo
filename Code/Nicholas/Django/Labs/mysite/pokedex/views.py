from django.shortcuts import render
from .models import Pokemon, PokemonType

def index(request):
    pokemon = Contact.objects.order_by('number')
    template = loader.get_template('pokedex/index.html')
    context = {
        'pokemon': pokemon,
    }
    return HttpResponse(template.render(context, request))
