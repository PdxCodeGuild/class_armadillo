from django.urls import path
from . import views

app_name = 'fishing'

urlpatterns = [
  path('index/', views.index, name='index')
]