from django.urls import path 
from . import views



app_name = 'pokedex'
urlpatterns = [
            path('', views.pokedex, name='pokedex')
]
 
