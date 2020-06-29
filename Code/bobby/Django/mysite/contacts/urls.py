from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "Contact"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
    path('new_contact/', views.new_contact, name='new_contact'),
    path('new_contact/submit/', views.submit, name='submit'),
]