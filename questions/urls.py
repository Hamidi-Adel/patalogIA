from django.urls import path, include
from . import views

app_name = 'questions'


urlpatterns = [
    path('',views.question, name='questiontype'),
    path('demarcate',views.createDemarcate, name='demarcatePage'),
    path('MCQs',views.MCQs, name='MCQsPage'),
    path('quiz',views.showQuestions, name='quiz'),
    path('quizdetail/<str:pk>', views.quizdetail, name='quizdetail'),
    path('demarcateQuiz', views.demarcateQuiz, name='demarcateQuiz'),
    path('demarcateQuizDetail/<str:pk>', views.demarcateQuizDetail, name = 'demarcateQuizDetail'),
    path('subjects/', views.subjects, name = 'subjects'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('marksheet/<str:pk>', views.totalMarks, name='marksheet'),

    path('pass', views.congrats, name = 'congrats'),
    path('fail', views.tryagain, name = 'tryagain'),

]
