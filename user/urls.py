from django.contrib import admin
from django.urls import path
from . import views;
from student import views as studentViews

urlpatterns = [
    path('', views.home,name='quiz-home'),
    path('login/', views.login,name='quiz-login'),
    path('registration/', views.register,name='quiz-regi'),
    path('main/',studentViews.dashboard,name='student-home'),
]