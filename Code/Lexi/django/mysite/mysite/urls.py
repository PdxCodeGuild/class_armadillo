from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('todo/', include('todo.urls')),
    path('pokedex/', include('pokedex.urls')),
    path('users/', include('users.urls')),
    # path('', include('main.urls'))
]