from django.urls import path
from . import views

app_name = 'todo_list'
urlpatterns = [
    
   
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('complete/', views.complete, name='complete'),
] 

