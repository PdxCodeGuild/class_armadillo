from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:code>/', views.redirect_url, name="redirect_url"),
]
