

from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_contact, name='create_contact'),
    path('create_contact_bootstrap/', views.create_contact_bootstrap, name='create_contact_bootstrap'),
    path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
]
