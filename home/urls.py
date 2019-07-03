from django.urls import path

from . import views

app_name = 'home'  # this app's name-space,
# app_name allows it to distinguish it's urls from same name urls of other app's in the same project
urlpatterns = [
    # ex: /cric_db_app/
    path('', views.index, name='index'),
    path('result',views.result, name="result")
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('doshit/<randomstring>/', views.doshit, name='doshit'),

]