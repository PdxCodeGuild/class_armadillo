from django.urls import path

from . import views

app_name = 'pokeapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pokemon_number>/', views.poke_detail, name='poke_detail'),
    path('search', views.search_pokemon, name='search_pokemon'),
    path('random', views.random_pokemon, name='random_pokemon'),
]