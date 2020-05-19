from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    return HttpResponse('you are at the index view of app 2')

def other(request):
    return HttpResponse('you are at the other view of app 2')