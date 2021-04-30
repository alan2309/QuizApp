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
    path('quizcreate/',views.QuizCreateView.as_view(),name='quizcreate'),
    path('quizdetail/<int:pk>/',views.QuizDetailView.as_view(),name='quizdetail'),
    path('quizdetail/<int:pk>/createquestion',views.QuestionCreateView.as_view(),name='questionadd'),
    path('delete/<int:pk>/',views.QuizDeleteView.as_view(),name='quizdelete'),
    path('create/<int:pk>/question/<int:p>/choice',views.ChoiceCreateView.as_view(),name='choiceadd'),
    path('api/data',views.ChartData.as_view(),name='api-data'),
    path('api/studentdata/<int:pk>/<str:p>',views.ChartStudentData.as_view(),name='api-studentdata'),
    path('api/questionadddata/<int:pk>',views.QuestionAdd.as_view(),name='api-questionadddata'),
    path('api/choiceadddata/<int:pk>/<int:p>',views.ChoiceAdd.as_view(),name='api-choiceadddata'),
]