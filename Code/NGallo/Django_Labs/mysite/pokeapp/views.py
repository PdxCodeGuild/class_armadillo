from django.shortcuts import render
from .models import Pokemon, PokemonType

def index(request):
    # getting all the pokemon by number
    pokemon_by_number = Pokemon.objects.order_by('number')
    context = {
        'pokemon_by_number': pokemon_by_number
    }
    return render(request,'pokeapp/index.html', context)

def poke_detail(request, pokemon_number):
    try:
        pokemon = Pokemon.objects.get(number=pokemon_number)
    except Pokemon.DoesNotExist:
        raise Http404("Pokemon does not exist")    
        
    context = {'pokemon': pokemon}
    return render(request, 'pokeapp/poke_detail.html', context)

# contacts.post for reference
def search_pokemon(request):
    
    name = request.POST['search']

    pokemon = Pokemon.objects.filter(name=pokemon_name)   
    # to return back to index you have to pass the same key to the template

    context = {
        'pokemon_by_number': pokemon_by_name
    }
    return render(request, 'pokeapp/index.html', context)