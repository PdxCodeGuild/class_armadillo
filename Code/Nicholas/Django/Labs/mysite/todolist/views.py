from django.shortcuts import render
from . models import TodoItem 


def index(request):
    todo_items = TodoItem.objects.order_by('created_date')
    context = {
        'todo_items': todo_items
    }
    return render(request, 'todolist/index.html', context)




