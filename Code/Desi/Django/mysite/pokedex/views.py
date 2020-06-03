from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    poke = Pokemon.objects.all()

    context = {'poke': poke}

    return render(request, 'pokedex/index.html', context)

def detail(request, poke):
    pokemon = Pokemon.objects.get(pk=poke)
    return render(request, 'pokedex/detail.htmol', {'poke': poke})


    # return HttpResponse('ok')

    
