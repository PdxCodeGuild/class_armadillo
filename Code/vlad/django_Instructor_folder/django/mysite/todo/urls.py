

from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    # localhost:8000/todo/
    path('', views.index, name='index'), 
    # localhost:8000/todo/create/
    path('create/', views.create, name='create'),
    # localhost:8000/todo/complete/5/
    # localhost:8000/todo/complete/89/
    path('complete/<int:todo_item_id>/', views.complete, name='complete'),
    # localhost:8000/todo/clear_completed/
    path('clear_completed/', views.clear_completed, name='clear_completed'),
    # localhost:8000/todo/delete/17/
    path('delete/<int:todo_item_id>/', views.delete, name='delete'),
    path('delete_via_form/', views.delete_via_form, name='delete_via_form'),
]