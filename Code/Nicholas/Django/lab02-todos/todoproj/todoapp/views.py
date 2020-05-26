from django.shortcuts import render
from .models import Todos 

def index(request):
    context={'message':'hello world!'}
    return render(request,'todoapp/index.html', context)