from django.shortcuts import render

from pokemon.models import Pokemon, PokemonType

def pokedex(request):
    if request.method == 'POST':
        query = request.POST['query']
        query_type = request.POST['query_type']

        if query_type == 'name':
            pokemon_list = Pokemon.objects.filter(name__icontains=query)
        elif query_type == 'poke_type':
            pokemon_list = Pokemon.objects.filter(types__name__icontains=query)
        elif query_type == 'number':
            pass
        
        print(pokemon_list)
    pokemon = Pokemon.objects.get(pk=123)
    types = ', '.join([typ.name for typ in pokemon.types.all()])

    context = {
        'pokemon': pokemon,
        'types': types,
    }

    return render(request, 'pokedex.html', context)