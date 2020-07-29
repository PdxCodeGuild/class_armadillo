
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_quote/', views.save_quote, name='save_quote'),
]


