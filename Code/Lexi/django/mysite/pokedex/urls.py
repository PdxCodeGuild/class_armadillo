from django.urls import path, include
from . import views
from django.contrib

app_name = 'pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pokemon_id>/', views.detail, name ='detail'),
]