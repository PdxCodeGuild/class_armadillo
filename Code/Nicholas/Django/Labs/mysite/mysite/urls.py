from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pokedex/', include('pokedex.urls')),
    path('contact_list/', include('contact_list.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
