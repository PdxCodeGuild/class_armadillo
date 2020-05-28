from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
  path('index/', views.index, name='index')
]