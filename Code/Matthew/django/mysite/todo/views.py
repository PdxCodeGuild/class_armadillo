from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import TodoItem

def index(request):
    todo_items = TodoItem.objects.order_by('completed_date')
    # print(todo_items)
    context =  {
        'title': 'Todo',
        'todo_items': todo_items,
    }
    return render(request, 'todo/index.html', context)


def create(request):
    # print(request.POST) # vertify we are receiving the form data

    # get todo text out of the form
    todo_text = request.POST['todo_text']
    # create an instance of our model
    todo_item = TodoItem(description=todo_text,
                            created_date=timezone.now(),
                            completed_date=None)
    # save the instance
    todo_item.save()
    # redirect to the index view 
    return HttpResponseRedirect(reverse('todo:index'))


def complete(request, todo_item_id):
    # look up the todo item with the given id
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    # set the completed date of that todo item
    todo_item.completed_date = timezone.now()
    # save the todo item
    todo_item.save()
    # redirect back to the index view
    return HttpResponseRedirect(reverse('todo:index'))