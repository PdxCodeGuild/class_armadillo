

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
    path('get_todos/', views.get_todos, name='get_todos'),
    path('get_priorities/', views.get_priorities, name='get_priorities'),
    path('index_form/', views.index_form, name='index_form'),
    path('create_todo_form/', views.create_todo_form, name='create_todo_form'),
    path('delete_todo_form/<int:todo_item_id>/', views.delete_todo_form, name='delete_todo_form'),
]

