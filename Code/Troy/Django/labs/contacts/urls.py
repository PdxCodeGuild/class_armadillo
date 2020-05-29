from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
    path('contacts/new/', views.new_contact, name='create'),
  ]
