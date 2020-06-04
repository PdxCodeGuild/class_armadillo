from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('you are at the index view of app 1')

def other(request):
    return HttpResponse('you are at the other view of app 1')