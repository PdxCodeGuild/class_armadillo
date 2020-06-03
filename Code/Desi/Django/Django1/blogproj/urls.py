from django.urls import path
from . import views

app_name = 'blogapp'
urlpattern = [
    path('index/' , view.index, name='index')
    path('admin/', admin.site.urls')
    path('blogapp/', include('blogapp.urls;))
    path('blogapp/', include('blogapp.urls;))
    path('blogapp/', include('blogapp.urls;))
]
