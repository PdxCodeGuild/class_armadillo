from django.shortcuts import render

from pokemon.models import Pokemon, PokemonType

def pokedex(request, poke_num = 0):
    pokemon=''
    types =''

    if poke_num > 0:
        pokemon = Pokemon.objects.get(number=poke_num)
        types = ', '.join([typ.name for typ in pokemon.types.all()])

    elif request.method == 'POST':
        query = request.POST['query']
        query_type = request.POST['query_type']

        if query_type == 'name':
            pokemon_list = Pokemon.objects.filter(name__icontains=query)
        elif query_type == 'poke_type':
            pokemon_list = Pokemon.objects.filter(types__name__icontains=query)
            query_type = 'type'
        elif query_type == 'number':
            pokemon_list = Pokemon.objects.filter(number=query)

        if len(pokemon_list) == 1:
            pokemon = pokemon_list[0]
            types = ', '.join([typ.name for typ in pokemon.types.all()])

            context = {
                'pokemon': pokemon,
                'types': types,
            }
        else:
            context = {
                'pokemon_list': pokemon_list,
                'query': query,
                'query_type': query_type,
            }

        return render(request, 'pokedex.html', context)
    #     print(pokemon_list)
    
    

    context = {
        'pokemon': pokemon,
        'types': types,
    }

    return render(request, 'pokedex.html', context)