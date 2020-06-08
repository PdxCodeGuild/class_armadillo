from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import random


def index(request):
    if request.method == 'POST':
        print(request.POST)
    context = {
        'title': 'Demo',
        'temperature': random.randint(50, 100),
        'fruits': ['apples', 'bananas', 'pears']
    }
    return render(request, 'demo/index.html', context)


def receive_form(request):
    print(request.POST)
    mytext = request.POST['mytext']
    return HttpResponse('ok')

def view1(request):
    return HttpResponse('view 1')

def view2(request):
    return HttpResponse('view 2')

def view3(request):
    return HttpResponse('view 3')

def view4(request, mynumber):
    return HttpResponse(f'your number is {mynumber}')

def view5(request, mystring):
    if mystring == 'paths1': # handle typos
        return HttpResponseRedirect(reverse('demo:view1'))
    return HttpResponse(f'your string is {mystring}')