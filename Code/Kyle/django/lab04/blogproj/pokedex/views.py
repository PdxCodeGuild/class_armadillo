from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    context = {
        'message': 'Gotta Catch em\' All!'
    }
    return render(request, 'pokedex/index.html', context)


