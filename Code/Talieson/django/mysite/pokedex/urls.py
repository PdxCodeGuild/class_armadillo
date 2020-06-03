from django.urls import path
from . import views


app_name = 'pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<name>/', views.details, name='details'),
]