from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('contacts/', include('contacts.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
