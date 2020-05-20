from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("IT WORRRRRKS! IT IS IN THE POLLSAPP INDEX, WE ARE")