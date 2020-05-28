from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    # first parameter - the path part of the url
    # second parameter - the view the path is connected to
    # third parameter - name of the route
    path('', views.index, name='index'),
    path('save_blog_post/', views.save_blog_post, name='save_blog_post')
]
