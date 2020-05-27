from django.shortcuts import render, get_object_or_404
from .models import Todos 

def index(request):
<<<<<<< HEAD
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
        
=======
    context={'message':'hello world!'}
    return render(request,'todoapp/index.html', context)
>>>>>>> 0717ae29682d538832a6b292251142be5a419d15
