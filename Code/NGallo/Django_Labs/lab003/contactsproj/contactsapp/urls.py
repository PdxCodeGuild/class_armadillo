from django.urls import path

from . import views

app_name = 'contactsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
    path('new/', views.addnew, name='new'),
    path('new/submit/', views.submit_form, name='submit'),
]