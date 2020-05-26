from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context =  {
        'title': 'Todo'
    }
    return render(request, 'todo/index.html', context)
