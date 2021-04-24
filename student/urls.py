from django.contrib import admin
from django.urls import path
from . import views
from user import views as userViews 

urlpatterns = [
    path('', views.dashboard,name='student-home'),
    path('logout/',userViews.logout,name='student-logout'),
    path('quiz/<int:quiz_id>/',views.quiz,name='enter-quiz'),
    path('test/<int:quiz_id>/',views.test,name='test-quiz'),
]