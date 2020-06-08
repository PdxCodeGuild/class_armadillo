from django.urls import path
from django.contrib import admin
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('index/', views.index, name='index'),
   
              ]