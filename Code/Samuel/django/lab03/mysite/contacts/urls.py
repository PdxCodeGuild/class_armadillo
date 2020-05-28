from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contacts_id>/', views.contacts_id, name='contacts_id'),
    path('new/', views.contacts_new, name='contacts_new'),
    path('new/submit/', views.contacts_new_submit, name='contacts_new_submit'),
]