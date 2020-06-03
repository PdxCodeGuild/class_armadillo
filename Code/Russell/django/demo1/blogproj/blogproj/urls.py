
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogapp/', include('blogapp.urls')),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls'))
]
