from django.urls import path
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('home/', views.index, name='home'),
    path('<int:pokemon_id>/', views.pokemon_id, name='pokemon_id'),
    path('pokemon_type/>', views.pokemon_type, name='pokemon_type'),
]