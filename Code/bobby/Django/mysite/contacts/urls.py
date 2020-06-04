from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "Contacts"
urlpatterns = [
    path('index/', views.index, name ='index'),
    path('add/', views.add, name='add'),
    path('save/', views.save, name='save'),
]