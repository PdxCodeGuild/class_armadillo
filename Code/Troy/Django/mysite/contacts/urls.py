from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


app_name = 'contacts'

urlpatterns = [
    path('index/', views.index, name='index'),
  ]
