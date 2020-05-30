from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:contacts_id>/', views.detail, name='detail'),
  path('new/', views.create_new_contact, name='create_new_contact'),
  path('save_contact/', views.save_post, name='save_post'),
]