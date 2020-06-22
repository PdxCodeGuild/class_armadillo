from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
    path('new/', views.new_contact, name='new_contact'),
    path('new/submit/', views.submit_contact, name='submit_contact'),
]