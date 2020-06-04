from django.shortcuts import render, reverse
from . models import TodoItem 
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    todo_items = TodoItem.objects.order_by('created_date')
    context = {
        'todo_items': todo_items
    }
    return render(request, 'todos/index.html', context)

def submit(request): 
    task = request.POST['task']
    if 'is_complete' in request.POST:
        is_complete = True
    else:
        is_complete = False 

    new_task = TodoItem(task=task,
                        is_complete=is_complete,) 
    new_task.save()

    return HttpResponseRedirect(reverse('todos:index'))   
