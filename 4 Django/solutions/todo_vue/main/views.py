from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Priority, TodoItem
import json


def index(request):
    return render(request, 'main/index.html')


def add_todo(request):

    # print(request.body)
    data = json.loads(request.body)
    # print(data)
    todo_text = data['todo_text']
    todo_priority_id = data['todo_priority_id']
    todo_item = TodoItem(text=todo_text, priority_id=todo_priority_id, completed_date=None)
    todo_item.save()
    
    # todo_text = request.GET['todo_text']
    # todo_priority_id = request.GET['todo_priority_id']
    # todo_item = TodoItem(text=todo_text, priority_id=todo_priority_id, completed_date=None)
    # todo_item.save()

    return HttpResponse('ok')

def get_priorities(request):
    priorities = []
    for priority in Priority.objects.all():
        priorities.append({
            'id': priority.id,
            'name': priority.name
        })
    return JsonResponse({'priorities': priorities})

def get_todos(request):
    todo_items = []
    for todo_item in TodoItem.objects.all():
        completed_date = None
        if todo_item.completed_date is not None:
            completed_date = todo_item.completed_date.strftime('%Y-%m-%d')
        todo_items.append({
            'id': todo_item.id,
            'text': todo_item.text,
            'priority': todo_item.priority.name,
            'created_date': todo_item.created_date.strftime('%Y-%m-%d'),
            'completed_date': completed_date
        })
    return JsonResponse({'todo_items': todo_items})


    # data = {
    #     'todo_items': TodoItem.objects.all()
    # }
    # return JsonResponse(data)
    # return JsonResponse({'name': 'bob', 'age': 34, 'fav color': 'red'})


def delete_todo(request):
    data = json.loads(request.body)
    todo_item_id = data['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.delete()
    return HttpResponse('ok')

def index_form(request):
    todo_items = TodoItem.objects.all()
    priorities = Priority.objects.all()
    context = {
        'todo_items': todo_items,
        'priorities': priorities,
    }
    return render(request, 'main/index_form.html', context)


def create_todo_form(request):
    print(request.POST)
    todo_text = request.POST['todo_text']
    todo_priority_id = request.POST['todo_priority_id']

    # priority = Priority.objects.get(id=todo_priority_id)
    # todo_item = TodoItem(text=todo_text, priority=priority, completed_date=None)

    todo_item = TodoItem(text=todo_text, priority_id=todo_priority_id, completed_date=None)
    todo_item.save()

    return HttpResponseRedirect(reverse('main:index_form'))

def delete_todo_form(request, todo_item_id):
    # print(todo_item_id)
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.delete()
    return HttpResponseRedirect(reverse('main:index_form'))
