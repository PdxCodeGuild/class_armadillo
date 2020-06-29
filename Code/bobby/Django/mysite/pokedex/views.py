from django.shortcuts import render, get_object_or_404, reverse
from .models import Pokemon
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
def index(request):
    page = request.Get.get('page', 1)
    pokemon = Pokemon.objects.order_by('number')
    if request.method == 'POST':
        search = request.POST['search']
        print(search)
        pokemon = Pokemon.objects.filter(name__icontains=search)
    
    context = {
        'title': 'Pokedex',
        'pokemon': 'pokemon',
    }    
    return render(request, 'pokedex/index.html', context)

def poke_index(request):
    pokemon = Pokemon.objects.order_by('number')
    
    return render(request, 'pokedex/index.html', context)
