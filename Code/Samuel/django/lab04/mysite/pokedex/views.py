from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    message = 'this is a test'
    context = {
        'message': message,
    }
    return render(request, 'pokedex/index.html', context)