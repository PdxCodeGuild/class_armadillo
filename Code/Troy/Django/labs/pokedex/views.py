from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pokemon, PokemonType
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator



def index(request):
    pokemon = Pokemon.objects.order_by('number')

    page = request.GET.get('page', 1)
    # pokemon = Pokemon.objects.filter('name').first()
    search= ''
    if request.method == 'POST':
        search = request.POST['search']

        pokemon = Pokemon.objects.filter(
        Q(name__icontains=search)| Q(number__icontains=search)
    )
    paginator = Paginator(pokemon, 10)
    pokemon = paginator.page(page)
    data = {
        'pokemon': pokemon,
        'search': search,
    }

    return render(request, 'pokedex/index.html', data)

def detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'pokedex/detail.html', {'pokemon':pokemon})

# def powers(request):
#     typ = pokemon_data

