

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_cities/', views.get_cities, name='get_cities')
]