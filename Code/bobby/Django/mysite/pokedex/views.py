from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'message': 'Hello Pokemon World'
    }
    return render(request, 'pokedex/index.html', context)