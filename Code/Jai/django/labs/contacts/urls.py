from django.urls import path

from .import views


appname = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.create, name='create'),
    path('<id>', views.detail),
    path('delete/<int:pk>', views.delete, name='contact_delete'),
    
    
]