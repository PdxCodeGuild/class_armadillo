# https://docs.djangoproject.com/en/3.0/intro/tutorial01/
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]