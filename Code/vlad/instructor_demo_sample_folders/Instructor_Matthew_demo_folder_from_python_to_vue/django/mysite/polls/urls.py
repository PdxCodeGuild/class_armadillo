from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/delete/ - receiving question id in form data
    path('delete/', views.delete, name='delete'),
    # ex: /polls/delete2/5/ - receiving question id in the path
    path('delete2/<int:question_id>/', views.delete2, name='delete2'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]