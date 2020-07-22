
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout_user'),
]

