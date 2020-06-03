from django.urls import path
from . import views


app_name = 'todoapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('save_todo', views.detail, name=''),
]