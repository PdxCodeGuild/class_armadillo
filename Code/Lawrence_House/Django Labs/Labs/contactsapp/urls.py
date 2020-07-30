from django.urls import path
from . import views

app_name = 'contactsapp'
urlpatterns = [
  path('index/', views.index, name='index'),
  path('<int:id>/', views.detail, name='detail'),
  path('new/', views.contactsnew, name='contactsnew'),
  # path('contacts/new/submit/', views.submit, name='submit'),
]