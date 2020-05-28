
from django.urls import path
from . import views

app_name = 'demo'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('receive_form/', views.receive_form, name='receive_form'),
    path('path1/', views.view1, name='view1'),
    path('path2/', views.view2, name='view2'),
    path('path3/', views.view3, name='view3'),
    path('<int:mynumber>/', views.view4, name='view4'),
    path('<str:mystring>/', views.view5, name='view5'),
]
