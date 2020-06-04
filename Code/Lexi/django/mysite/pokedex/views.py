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
        pokemon = Pokemon.objects.filter(Q(name='search') | Q(number=search)
        )
        data = {
            'pokemon': pokemon,
            'search': search,
        }
        print(request.POST)
        return render(request, 'pokedex/index.html', data)

def detail(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'pokedex/detail.html',{'pokemon':pokemon})

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
