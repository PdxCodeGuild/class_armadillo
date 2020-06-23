from django.urls import path, include   
from . import views


app_name = 'contactlist'

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('create_contact', views.create_contact, name='create_contact'),
    path('contact_details/<int:id>/', views.details, name='details'),
    path('update_contact/<int:id>/', views.update, name='update_contact'),
    path('delete/<int:pk>', views.delete, name='contact_delete')
    
]