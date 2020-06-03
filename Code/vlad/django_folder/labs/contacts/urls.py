from django.urls import path
from . import views
from django.contrib import admin

app_name = 'contacts'
urlpatterns = [
  path('', views.index, name='index'), # the Url path is ''
  path('<int:contact_id>/', views.detail, name='detail'), # the Url path is '<int:contact_id>/'
  path('new/', views.create_contact_page, name='new'),  # the Url path 'new/' which tight the contact_new.html
  path('new/submit/', views.create_contact, name='create') # the Url path is 'new/submit/'
]

# the views.py function names will be here for the url.py for example = path('new/submit/', views.create_contact, name='create')