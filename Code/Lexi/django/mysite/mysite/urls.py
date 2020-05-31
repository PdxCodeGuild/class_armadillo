from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),



    
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]