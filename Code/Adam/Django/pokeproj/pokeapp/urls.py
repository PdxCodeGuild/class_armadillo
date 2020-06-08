

from django.urls import path

from . import views

app_name = 'pokeapp'
urlpatterns = [
    path('index/', views.index, name='index')
]