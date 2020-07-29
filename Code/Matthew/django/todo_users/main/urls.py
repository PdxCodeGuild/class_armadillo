
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.list, name='list'),
    path('todos/<int:todo_item_id>/', views.detail, name='detail'),
]

