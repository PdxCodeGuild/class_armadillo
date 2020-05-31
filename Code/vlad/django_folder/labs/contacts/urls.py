from django.urls import path
from . import views
from django.contrib import admin

app_name = 'contacts'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:contact_id>/', views.detail, name='detail'),
  path('new/', views.contact_new, name='create_new_contact'),  
  path('new/submit/', views.create_new_contact, name='create_new_contact')