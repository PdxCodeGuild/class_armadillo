from django.core.paginator import Paginator
from django.shortcuts import render
from pokemon.models import Pokemon, PokemonType

def pokedex(request, poke_num = 0):

    query = request.GET.get('query', '')
    query_type = request.GET.get('query_type', 'name')

    if poke_num > 0:
        pokemon = Pokemon.objects.get(number=poke_num)
        types = ', '.join([typ.name for typ in pokemon.types.all()])
        
        context = {
            'pokemon': pokemon,
            'types': types,
            'query_type':query_type
        }

        return render(request, 'pokedex.html', context)

    if request.method == 'POST':
        query = request.POST['query'].strip()
        query_type = request.POST['query_type']
    else:
        query = request.GET.get('query', '')
        query_type = request.GET.get('query_type', 'poke_type')
    
    print(f'{query_type = }')

    if query == '':
        context = {
            'query_type': query_type,
        }
        return render(request, 'pokedex.html', context)

    if query_type == 'name':
        pokemon_list = Pokemon.objects.filter(name__icontains=query)
    elif query_type == 'poke_type':
        pokemon_list = Pokemon.objects.filter(types__name__icontains=query)
    elif query_type == 'number':
        if query.isdigit():
            pokemon_list = Pokemon.objects.filter(number=query)
        else:
            pokemon_list = Pokemon.objects.filter(name='farts')

    

    paginator = Paginator(pokemon_list, 5)
    page = request.GET.get('page', 1)

    print(page)

    pokemon_page = paginator.get_page(page)

    if len(pokemon_page.object_list) == 1:
        pokemon = pokemon_list[0]
        types = ', '.join([typ.name for typ in pokemon.types.all()])
        context = {
            'pokemon': pokemon,
            'types': types,
            'query_type':query_type
        }

        return render(request, 'pokedex.html', context)

    context = {
        'pokemon_list': pokemon_page,
        'query': query,
        'query_type': query_type,
    }

    return render(request, 'pokedex.html', context)

    

    