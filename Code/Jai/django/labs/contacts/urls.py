from django.urls import path

from .import views


appname = 'contacts'
urlpatterns = [
    path('', views.index, name='index')
    
    
]