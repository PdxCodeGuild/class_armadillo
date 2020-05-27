from django.shortcuts import render
from .models import Todos 

def index(request):
    todos = Todos.objects.order_by('publish_date')
    context={
        'todos': todos
    }
    return render(request,'todoapp/index.html', context)