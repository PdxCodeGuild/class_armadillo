from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    return HttpResponse('you are at the index of app 2')
