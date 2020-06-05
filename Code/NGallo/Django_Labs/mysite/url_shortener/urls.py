from django.urls import path
from . import views

app_name = 'url_shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('<str:code>/', views.redirect, name='redirect'),
]