from django.shortcuts import render

def pokedex(request):
    context = {}
    return render(request, 'pokedex.html', context)