from django.shortcuts import render, get_object_or_404
from .models import Todos 

def index(request):
    todos = Todos.objects.order_by('publish_date')
    completed = Todos.objects.order_by('completed_date')
    context={
        'todos': todos
    }
    return render(request,'todoapp/index.html', context)

def detail(request, todos_id):
    todo = get_object_or_404(Todos, pk=todos_id)
    completed = Todos.objects.order_by('completed_date')
    return render(request,'todoapp/index.html', context)
        