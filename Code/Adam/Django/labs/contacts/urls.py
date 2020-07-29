from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
  path('base/', views.base, name='base'),
  path('', views.index, name='index'),
  path('<int:contact_id>/', views.detail, name='detail'),
  path('new/', views.new, name='new'),
  path('new/save/', views.new_save, name='new_save'),
]