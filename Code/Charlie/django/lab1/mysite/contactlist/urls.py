from django.urls import path, include   
from . import views


app_name = 'contactlist'

urlpatterns = [
    path('create_contact', views.create_contact, name='create_contact'),
    path('', views.contacts, name='contacts'),
    path('contact_details/<int:id>/', views.details, name='details'),
    path('update_contact/<int:id>/', views.update, name='update_contact'),
    
]