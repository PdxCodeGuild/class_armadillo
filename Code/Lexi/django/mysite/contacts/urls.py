from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #  localhost:8000/5/
    path('<int:contact_id>/', views.detail, name='detail'),
   path('new/', views.entry_page, name='entry_page'),
    path('new/submit/', views.submit_contact, name='submit_contact'),
]