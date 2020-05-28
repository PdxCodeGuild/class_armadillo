from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    chores = TodoItem.objects.all().order_by('created_date')

    context = {
        'chores': chores,
    }

    return render(request, 'todo_list/index.html', context)




def delete(request):
    chore_id = request.POST['delete']
    chore = TodoItem.objects.get(id=chore_id)
    chore.delete()

    return HttpResponseRedirect(reverse('todo_list:index'))

def create(request):
    name = request.POST['name']
    description = request.POST['description']
    priority = request.POST['priority']
    TodoItem.objects.create(name=name, description=description, priority=priority)

    return HttpResponseRedirect(reverse('todo_list:index'))

def complete(request):
    chore_id = request.POST['id']
    chore = TodoItem.objects.get(id=chore_id)
    chore.status = True
    chore.save()
    print(chore)
    return HttpResponseRedirect(reverse('todo_list:index'))
