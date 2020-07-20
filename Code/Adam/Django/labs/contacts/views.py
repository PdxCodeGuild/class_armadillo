from django.shortcuts import render

# Create an index view
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world!')