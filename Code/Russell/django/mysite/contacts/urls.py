from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>', views.details, name='details' ),
    path('new/', views.new, name='new'),
    path('save/submit/', views.save_submit, name='save_submit')
]