
from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('new/submit/', views.new_submit, name='new_submit'),
    path('delete/<int:contact_id>/', views.delete, name='delete'),
    path('edit/<int:contact_id>/', views.edit, name='edit'),
    path('edit/submit/', views.edit_submit, name='edit_submit'),
]
