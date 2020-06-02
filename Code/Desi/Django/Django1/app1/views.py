from django.urls import path
from . import views

def index(request):
    return HttpResponse('you are at the index view of app2')