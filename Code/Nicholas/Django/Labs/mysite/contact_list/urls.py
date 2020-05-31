from django.urls import path
from . import views

app_name = 'contact_list'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
]