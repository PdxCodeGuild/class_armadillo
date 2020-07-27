from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
  path('base/', views.base, name='base'),
  path('', views.index, name='index'),
]