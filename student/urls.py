from django.contrib import admin
from django.urls import path
from . import views
from user import views as userViews 

urlpatterns = [
    path('', views.dashboard,name='student-home'),
    path('logout/',userViews.logout,name='student-logout'),
    path('quiz/<int:quiz_id>/',views.quiz,name='enter-quiz'),
    path('test/<int:quiz_id>/',views.test,name='test-quiz'),
    path('results/<int:quiz_id>/',views.results,name='result-quiz'),
    path('records/<int:quiz_id>/',views.records,name='student-records'),
    path('quiz/',views.QuizListView.as_view(),name='quizlist'),
    path('quizcreate/',views.QuizCreateView.as_view(),name='quizcreate'),
    path('quizdetail/<int:pk>/',views.QuizDetailView.as_view(),name='quizdetail'),
    path('quiz/createquestion/<int:pk>/',views.QuestionCreateView.as_view(),name='questionadd'),
    path('quiz/delete/<int:pk>/',views.QuizDeleteView.as_view(),name='quizdelete'),
    path('quiz/create/<int:pk>/question/<int:p>/choice',views.ChoiceCreateView.as_view(),name='choiceadd'),
]