from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import TodoItem, Priority

def index(request):
    todo_items = TodoItem.objects.order_by('completed_date')
    priorities = Priority.objects.all()
    context =  {
        'title': 'Todo',
        'todo_items': todo_items,
        'priorities': priorities,
    }
    return render(request, 'todo/index.html', context)


def create(request):
    print(request.POST) # vertify we are receiving the form data

    # get todo text out of the form
    todo_text = request.POST['todo_text']
    priority_id = request.POST['priority_id']
    # create an instance of our model
    todo_item = TodoItem(description=todo_text,
                            created_date=timezone.now(),
                            completed_date=None,
                            priority_id=priority_id)
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

def clear_completed(request):
    # get all the todo items whose completed date is null
    completed_items = TodoItem.objects.filter(completed_date__isnull=False)
    # delete them
    completed_items.delete()
    # redirect back to the index page
    return HttpResponseRedirect(reverse('todo:index'))


def delete(request, todo_item_id):
    # look up the todo item with the given id
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    # delete the todo item
    todo_item.delete()
    # redirect back to the index page
    return HttpResponseRedirect(reverse('todo:index'))

def delete_via_form(request):
    print(request.POST)
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    todo_item.delete()
    # redirect back to the index page
    return HttpResponseRedirect(reverse('todo:index'))
