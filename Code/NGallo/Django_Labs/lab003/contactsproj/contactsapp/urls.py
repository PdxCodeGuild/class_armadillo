from django.urls import path

from . import views

app_name = 'contactsapp'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.details, name='details'),
]