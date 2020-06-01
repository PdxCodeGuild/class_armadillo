from django.urls import path 
from . import views



app_name = 'pokedex'
urlpatterns = [path('index/', views.index, name='index')
)


]

