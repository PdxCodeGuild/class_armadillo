from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import TodoItem, Priority


def index(request):
    return render(request, 'main/index.html')

@login_required
def list(request):
    # todos = TodoItem.objects.all()
    # todos = TodoItem.objects.filter(user=request.user)
    todos = request.user.todo_items.all()
    context = {
        'todos': todos
    }
    return render(request, 'main/list.html', context)

@login_required
def detail(request, todo_item_id):
    # todo = TodoItem.objects.filter(pk=todo_item_id, user=request.user).first()
    # todo = request.user.todo_items.filter(pk=todo_item_id).first()
    todo = get_object_or_404(TodoItem, pk=todo_item_id, user=request.user)
    return render(request, 'main/detail.html', {'todo': todo})