from django.urls import path
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('home/', views.index, name='home')
]