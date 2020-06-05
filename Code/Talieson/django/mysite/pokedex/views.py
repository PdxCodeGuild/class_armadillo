from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Pokemon, PokemonType

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    pokemon = Pokemon.objects.order_by('number')
    if request.method =='POST':
        search = request.POST['search']
        print(search)
        pokemon = Pokemon.objects.filter(name__icontains=search)
        pokemon = pokemon.order_by('number')
    
    paginator = Paginator(pokemon, 10)
    pokemon = paginator.page(page)

    context = {
        "Pokemon": pokemon,
        }
    return render(request, 'index.html', context)


def details(request, name):
    pokemon_details = Pokemon.objects.get(name=name)
    context = {
        "pokemon_details": pokemon_details,
    }
    return render(request, "details.html", context)


