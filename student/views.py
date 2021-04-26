from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .models import Quiz,Question,Result,Choice
from datetime import datetime
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib import messages



class QuizListView(ListView):
    context_object_name='quizs'
    model=Quiz
    template_name='student/listquiz.html'

class QuizCreateView(CreateView):
    fields=('quiz_subject','quiz_name','quiz_end','quiz_time')
    model=Quiz
    template_name='student/quizadd.html'
    
    success_url=reverse_lazy('quizlist')


class QuizDetailView(DetailView):
    context_object_name='quiz_detail'
    model=Quiz
    template_name='student/quiz_detail.html'
    success_url=reverse_lazy('quizlist')

    
class QuestionCreateView(CreateView):
    fields=('quiz','question_text')
    model=Question
    template_name='student/quizadd.html'

class QuizDeleteView(DeleteView):
    model=Quiz
    template_name='student/quiz_confirm_delete.html'
    success_url=reverse_lazy('quizlist') 

class ChoiceCreateView(CreateView):
    fields=('question','choice_text','ans')
    model=Choice
    template_name='student/quizadd.html'


@login_required
def dashboard(request):
    open_quizzes = Quiz.objects.filter(quiz_end__gte = datetime.now().date())
    closed_quizzes  = Quiz.objects.filter(quiz_end__lt = datetime.now().date())
    return render(request,'student/dashboard.html',{'open_quizzes':open_quizzes,'closed_quizzes':closed_quizzes})

def quiz(request,quiz_id):
    quiz = Quiz.objects.get(id = quiz_id)
    if quiz.result_set.filter(student_email = request.POST['email']).exists():
        return render(request,'student/student-result.html',{
            'result': quiz.result_set.get(student_email = request.POST['email']).student_marks,
            'total': quiz.result_set.get(student_email = request.POST['email']).total_marks,
            })
    else: 
        if request.POST['status'] == "closed":
            return render(request,'student/student-result.html',{
            'result': -1,
            'total': 0,
            })
        else:    
            return render(request,'student/quiz.html',{'quiz_id':quiz_id,'time':float(quiz.quiz_time)})    

def test(request,quiz_id):
    name = request.POST['name']
    sap = request.POST['sap']
    time = request.POST['time']
    quiz = Quiz.objects.get(id=quiz_id)
    questions_list = quiz.question_set.all()

    return render(request,'student/test.html',{
        'time':time,
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
        try:
            x = request.POST[question.question_text] 
            if  x == "True":
                results+=1
        except:
            pass
   
    x=quiz.result_set.create(student_email=request.POST['email'],student_marks=str(results),student_name=request.POST['name'],student_sap=request.POST['sap'],quiz=quiz_id,total_marks=str(total))
    x.save()

    return render(request,'student/results.html',{'result':results,'sap':request.POST['sap'],'total':total})

@login_required
def adminDash(request):
    return render(request,'student/admin_dash.html',{'quizzes':Quiz.objects.all()})    

def records(request,quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    records = quiz.result_set.all()
    return render(request,'student/records.html',{'quiz_id':quiz_id,'records':records})    