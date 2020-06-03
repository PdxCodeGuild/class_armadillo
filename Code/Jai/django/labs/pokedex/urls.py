from django.urls import path 
from . import views



app_name = 'pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pokemon_number>/', views.detail, name='detail')
]
 
