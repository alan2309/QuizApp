from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import Quiz,Question
from datetime import datetime

@login_required
def dashboard(request):
    return render(request,'student/dashboard.html',{'quizzes':Quiz.objects.all()})

def quiz(request,quiz_id):
    return render(request,'student/quiz.html',{'quiz_id':quiz_id})    

def test(request,quiz_id):
    name = request.POST['name']
    sap = request.POST['sap']
    quiz = Quiz.objects.get(id=quiz_id)
    questions_list = quiz.question_set.all()
    

    return render(request,'student/test.html',{
        'sap':sap,
        'name':name,
        'questions_list':questions_list,
        'quiz_id':quiz_id
    })    

def results(request,quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.question_set.all()
    results=0
    total=questions.count()
    for question in questions:
        x = request.POST[question.question_text]
        
        if  x == "True":
            print(request.POST[question.question_text])
            results+=1

    return render(request,'student/results.html',{'result':results,'total':total})   