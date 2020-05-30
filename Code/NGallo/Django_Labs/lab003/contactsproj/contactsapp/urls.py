from django.urls import path

from . import views

app_name = 'contactsapp'

urlpatterns = [
    path('index/', views.index, name='index')
]