from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #  localhost:8000/5/
    path('<int:contact_id>/', views.detail, name='detail'),
    path('new/', views.create_contact_page,
    name= 'create_new_contact'),
]