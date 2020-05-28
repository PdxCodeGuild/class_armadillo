from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse('hello world!') # in order to see hello world I needed to use the following URL: http://localhost:8000/contacts/index/