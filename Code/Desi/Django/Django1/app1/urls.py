from django.urls import path
from . import views

app_name = 'blogapp'
urlpattern = [
    path('index/' , view.index, name='index')
    path(other/', views.other, name='other')
    
    