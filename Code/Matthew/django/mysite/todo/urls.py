

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
    path('complete/<int:todo_item_id>/', views.complete, name='complete')
]