
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('todo/', include('todo.urls')),
    path('blogapp/', include('blogapp.urls')),
    path('demo/', include('demo.urls')),
    path('contacts/', include('contacts.urls')),
    path('pokedex/', include('pokedex.urls')),
    path('', include('main.urls')), # the request will go to this one if it doesn't match any others
]
