from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pokedex(request):
    return HttpResponse('Hello Pokemon World')