from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def index(request):
    context = {
        'message': 'Jello WOrld!'


    }
    return render(request, 'blogapp/index.html', context)
