from django.urls import path

from . import views

app_name = 'polls' # namespace 추가

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/',views.detail,name='detail'), # ex: /polls/5
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
]
