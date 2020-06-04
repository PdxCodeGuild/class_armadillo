from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Pokemon, PokemonType

# Create your views here.
def index(request):
    
    if request.method =='POST':
        search = request.POST['search']
        pokemon = Pokemon.filter(name__icontains=search)
        context = {"Pokemon": pokemon.objects.order_by('number')}
    paginator = Paginator(Pokemon, 10)
    page = paginator.page(1)
    pokemon = page.object_list
    context = {"Pokemon": Pokemon.objects.order_by('number')}
    return render(request, 'index.html', context)


def details(request, name):
    pokemon_details = Pokemon.objects.get(name=name)
    context = {
        "pokemon_details": pokemon_details,
    }
    return render(request, "details.html", context)


