from django.urls import path, include   
from . import views


app_name = 'contactlist'

urlpatterns = [
    path('', views.index, name='contacts'),
    path('<int:card_id>/', views.detail, name='detail'),
    path('new/', views.entry_page, name='entry_page'),
    path('new/submit/', views.create_contact, name='create_contact'),
    path('delete/<int:card_id>/', views.delete, name='delete'),
    path('edit/<int:card_id>/', views.edit_page, name='edit_page'),
    path('edit/submit/', views.submit_update, name='submit_update')
]