from django.core.paginator import Paginator
from django.shortcuts import render
from pokemon.models import Pokemon, PokemonType

def pokedex(request, poke_num = 0):
    pokemon=''
    types =''
    # pokemon_list = Pokemon.objects.all()
    query_type = request.GET.get('query', 'name')

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

    if query_type == 'name':
        pokemon_list = Pokemon.objects.filter(name__icontains=query)
    elif query_type == 'poke_type':
        pokemon_list = Pokemon.objects.filter(types__name__icontains=query)
        query_type = 'type'
    elif query_type == 'number':
        pokemon_list = Pokemon.objects.filter(number=query)
    
    paginator = Paginator(pokemon_list, 5)
    page = request.GET.get('page', 1)
    pokemon_page = paginator.get_page(page)

    context = {
        'pokemon_list': pokemon_page,
        'query': query,
        'query_type': query_type,
    }

    print(f'{query = }')

    return render(request, 'pokedex.html', context)
#     print(pokemon_list)

    

    