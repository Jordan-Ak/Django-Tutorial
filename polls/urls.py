from django.urls import path

from . import views

app_name = 'polls'


urlpatterns = [
 #Index page
    path('', views.IndexView.as_view(), name='index'),
#Detailed question
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#Results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#Votes
    path('<int:question_id>/vote/', views.vote, name='vote'),
]