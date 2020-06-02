from django.shortcuts import render

def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'pokeapp/index.html', context)

