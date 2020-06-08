from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Pokemon, PokemonType
from django.db.models import Q
from django.core.paginator import Paginator

# Paginator resource =  https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
# we want the paginator to start on the home page which is the index page. this is why we put the paginator under the index view
# Create your views here.


def index(request):
    # this is the name of my app Pokemon
    pokemon = Pokemon.objects.order_by('name')
    # Make a request to the page with GET because we are getting the page instead of post from the browser this is why is it is capital GET
    # page is one of the string objects and 1 is the page the page starts this is what is going to be display at the button of my page
    page = request.GET.get('page', 1)

    # paginator need to be done before the context variable below if do it after it will not show
    # create a variable and bring the model from line 6 Paginator
    paginator = Paginator(pokemon, 20)  # this will print 20 pokemons per page
    # this is saying for every 15 pokemon I need to create a new page
    pokemon = paginator.page(page)

    context = {
        'pokemons': pokemon

    }
    # query = ""
    if request.method == "POST":
        query = request.POST['q']
        # print(type(query))
        pokes = Pokemon.objects.filter(
            Q(name__icontains=query)
            # icontain will eliminate any capitalization types__number__icontains
            | Q(number__icontains=query)
            | Q(height__icontains=query)
            | Q(weight__icontains=query)
            | Q(image_front__icontains=query)
            # icontain will eliminate any capitalization
            | Q(image_back__icontains=query)
            | Q(types__name__icontains=query))
        context['query'] = pokes

    return render(request, 'pokedex/index.html', context)


def detail(request, pokemon_id):  # contact_id each person have a unique contact_id
    # I am searching by number
    pokemon = get_object_or_404(Pokemon, number=pokemon_id)
    types = []  # make a list of just the types
    for type in pokemon.types.all():
        print(type)
        types.append(type.name)

    # {'contact': contact}) this is giving a single contact this is why is singular because when we click the name of one of the people in the contact list it will give only that person contact details instead of everyone else
    # to get a list of the types to turn the query set of the types into a list: list(pokemon.types.all())
    return render(request, 'pokedex/detail.html', {'pokemon': pokemon, 'types': ', '.join(types)})


# adding a search button on the index page:


def search(query=None):
    queryset = []
    # this will do the search and divide the results with the coma
    queries = query.split(" ")
    # create a loop to search for the query:
    for q in queries:
        pokes = Pokemon.objects.filter(Q(types__name__icontains=q)
                                       # icontain will eliminate any capitalization types__number__icontains
                                       | Q(types__number__icontains=q)
                                       | Q(types__heigh__icontains=q)
                                       | Q(types__weight__icontains=q)
                                       | Q(types__image_front__icontains=q)
                                       # icontain will eliminate any capitalization
                                       | Q(types__image_back__icontains=q)
                                       | Q(types__types__icontains=query))  # .distinct()  # make it distint so all the searches are unique

    for poke in pokes:  # to loop through each of the query
        queryset.append(poke)  # to add the to the query set
    # set will make sure the return is unique and then it is converted into a list that can be used in the template
    return list(set(queryset))


# on line 22 create an empty list then loop each pokemon.types.all
# then append the name of each type to the list
# this will give me the name
# in the template detail I can use the join method
# Using list comprehension way to do it below:
# #types = ', '.join([p_type.name for p_type in pokemon.types.all()])


# # def create_pokemon_page(request):
#     return render(request, 'pokemon/new_pokemon.html')
