from django.urls import path
from . import views

app_name = 'app2'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('other/', views.other, name='other')
]
