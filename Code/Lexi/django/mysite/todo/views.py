from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import TodoItem


# this view helps us render data in the template
def index(request):
    chores = TodoItem.objects.all().order_by('created_date')

    context = {
        'chores': chores,
    }
    return render(request, 'todo/index.html', context)

# this view helps us go back a page after finding the chore
# we wish to delete via template ID
def delete(request):
    chore_id = request.POST['chore_id']
    chore = TodoItem.objects.get(id=chore_id)
    chore.delete()

    return HttpResponseRedirect(reverse('todo_list:index'))

# this view creates
def create(request):
    name = request.POST['name']
    description = request.POST['description']
    priority = request.POST['priority']
    todo_item = TodoItem(name=name, description=description, priority=priority)
    todo_item.save()

    return HttpResponseRedirect(reverse('todo_list:index'))

# this view indicated completion
def complete(request):
    chore_id = request.POST['id']
    chore = TodoItem.objects.get(id=chore_id)
    chore.status = True
    chore.save()
    print(chore)
    return HttpResponseRedirect(reverse('todo_list:index'))
