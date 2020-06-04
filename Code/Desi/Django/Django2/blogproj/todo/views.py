from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo

# Create your views here.
def index(request):
    List = Todo.objects.all().order_by('completed_date')

    context = {
        'title': 'Todo',
        'list': list, 
    }

    return render(request, 'List/index.html', context)


    def create(request):
        print(request.POST) #verify we are receiving the form data

        todo_list = request.POST['todo_text']
        priority = request.POST['priority']
        # create an instance of model
        todos = todo(description=todo_text,
                        created_date=timezone.now(),
                        completed_date=none,
                        priority = priority,
                        )
                        
        # save the instance
        todos.save()
        # redirect to the index value
        return HttpResponseRedirect(reverse('todo:index'))

    def complete(request, todo)