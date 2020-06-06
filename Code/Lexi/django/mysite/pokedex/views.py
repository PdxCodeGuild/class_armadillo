from django.shortcuts import render, get_object_or_404
from .models import Pokemon, PokemonType
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Q

def index(request):

    pokemon = Pokemon.objects.all().order_by('name')
    search = ''
    if request.method == 'POST':
        search = request.POST['search']
        pokemon = Pokemon.objects.filter(Q(name__icontains=search) )
    data = {
        'pokemon': pokemon,
        'search': search,
    }
    # print(request.POST()) <--this does NOT WORK
    print(pokemon) #<QuerySet [<Pokemon: abra 63>,
    return render(request, 'pokedex/index.html', data)

# changed from 'id' which is a primary key to the actual pokemon number
def detail(request, number):
    # had pk=pokemon_id but that generates something similar to counter
    pokemon = get_object_or_404(Pokemon, number=number)
    # try to get queryset of types from models
    # types = models.ManyToManyField('PokemonType', related_name='pokemon')
    types = pokemon.types.all() #parse and iterate
    print(types)


    context = {
        'pokemon': pokemon,
        'types' : types,
    }
    # typ = ''
    # for typ in types:
    #     typ.append(types)
    # print(types)

    return render(request, 'pokedex/detail.html', context)



# <QuerySet [<PokemonType: fire>]>
# treat it as list inside django template





# FIRST INDEX CREATED FOR THIS LAB
# def index(request):

#     context = {
#         "pokemon": Pokemon.objects.order_by('number')}
    
#     return render(request, 'pokedex/index.html', context)

# SECOND INDEX CREATED FOR THIS LAB
# def index(request):
#     pokemon = Pokemon.objects.order_by('number')
#     search = 75
#     pokemon = Pokemon.objects.filter(
#         Q(name='search') | Q(number=search)
#         )
#     data = {
#         'pokemon': pokemon,
#         'search': search,
#     }
    
#     return render(request, 'pokedex/index.html', data)

# THIRD INDEX CREATED FOR THIS LAB
# def pokemon_type(request):
#     list_of_pokemon = Pokemon.objects.filter(Q(name__icontains=request.POST['search']) | Q(types__name__icontains=request.POST['search'].lower()))

#     template = loader.get_template('pokedex/types.html')
#     context = {
#         'list_of_pokemon': list_of_pokemon,
#         'query': request.POST['search']
#     }
#     return HttpResponse(template.render(request, context))
