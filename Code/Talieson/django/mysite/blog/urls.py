from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog'),
    path('new/', views.create_post_page, name='create_post_page'),
]