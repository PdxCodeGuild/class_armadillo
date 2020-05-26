from django.shortcuts import render
from django.html import HttpResponse

def index(request):
    return HttpResponse('hello world')
