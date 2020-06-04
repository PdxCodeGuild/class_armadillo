from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    context = {
        'title': 'My Blog'
    }

    return render(request, 'blogapp/index.html', context)
    # return HttpResponse('hello world')
