from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Quiz,Question,Result,Choice
from datetime import datetime
from django.views.generic import (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from django import forms

class ChartData(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        res = []
        a = []
        quizs = Quiz.objects.all()
        for quiz in quizs:
            if quiz.quiz_subject not in res:
                res.append(str(quiz.quiz_subject))
                resindex=res.index(str(quiz.quiz_subject))
                a.append(1)
            else :
                aindex=res.index(str(quiz.quiz_subject))
                a[aindex]=a[aindex]+1
        chartLabel = "Data"
        data ={
                     "chartdata":a,
                     "labels":res,
                     "chartLabel":chartLabel,   
             }
        return Response(data)

class ChartStudentData(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        res = []
        a=[]
       
        results = Result.objects.filter(quiz=kwargs['pk'],student_email=kwargs['p'])
        resultsf = Result.objects.filter(quiz=kwargs['pk'])
        count=[]

        for result in resultsf:
            count.append(result.student_marks)
        if resultsf.exists():
            maxMarks=max(count)
            a.append(maxMarks)
            res.append("MaxMarks")

        for result in results:
            res.append(str(result.student_email))
            a.append(str(result.student_marks))
        if resultsf.exists():   
            minMarks=min(count)
            a.append(minMarks)
            res.append("MinMarks")
            
        chartLabel = "Data"
        data ={
                     "chartdata":a,
                     "labels":res,
                     "chartLabel":chartLabel,   
             }
        return Response(data)

class QuestionAdd(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        res = []
        quizid=Quiz.objects.filter(id=self.kwargs['pk'])
        for quiz in quizid:
            res.append(quiz.id)

        data ={
                     "quizapi":res,  
             }
        return Response(data)

class ChoiceAdd(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self,request,*args,**kwargs):
        a=[]
        quizid=Quiz.objects.filter(id=self.kwargs['pk'])
        questionid=Question.objects.filter(id=self.kwargs['p'])
        for question in questionid:
            a.append(question.id)
        data ={
                     "questionapi":a, 
             }
        return Response(data)




class QuizListView(ListView):
    context_object_name='quizs'
    template_name='student/admin_dash.html'
    model=Quiz
    def get_context_data(self, **kwargs):
        context = super(QuizListView, self).get_context_data(**kwargs)
        context['questions_list'] = Question.objects.all()
        context['results_list'] = Result.objects.all()
        return context
       

class QuizCreateView(CreateView):
    fields=('quiz_subject','quiz_name','quiz_end','quiz_time')
    model=Quiz
    template_name='student/quizadd.html'
    success_url=reverse_lazy('admin-dash')


class QuizDetailView(DetailView):
    context_object_name='quiz_detail'
    model=Quiz
    template_name='student/quiz_detail.html'

    
class QuestionCreateView(CreateView):
    fields=('quiz','question_text')
    model=Question
    template_name='student/quizadd.html'
    def get_context_data(self, **kwargs):
        txt=self.request.get_full_path()
        x = txt.split(str(self.kwargs['pk']))
        
        url1=self.request.get_full_path()
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['url'] = x[0]
        id=Quiz.objects.filter(id=self.kwargs['pk'])
        context['Lquiz'] = id
        context['qid']=self.kwargs['pk']
        context['url1']=url1
        return context

class QuizDeleteView(DeleteView):
    model=Quiz
    template_name='student/quiz_confirm_delete.html'
    success_url=reverse_lazy('admin-dash') 

class ChoiceCreateView(CreateView):
    model = Choice
    fields=['question','choice_text','ans']
    template_name='student/quizadd.html'
    def get_context_data(self, **kwargs):
        id=Question.objects.filter(id=self.kwargs['p'])
        context = super(ChoiceCreateView, self).get_context_data(**kwargs)
        context['Lquestion'] = id
        context['qid']=self.kwargs['pk']
        context['questionid']=self.kwargs['p'] 
        return context
    

@login_required
def dashboard(request):
    open_quizzes=[]
    closed_quizzes=[]
    quizzes = Quiz.objects.all()
    for quiz in quizzes:
        if quiz.result_set.filter(student_email = request.user.email).exists() or quiz.quiz_end < datetime.now().date():
            closed_quizzes.append(quiz)
        else:    
            open_quizzes.append(quiz)
    return render(request,'student/dashboard.html',{'open_quizzes':open_quizzes,'closed_quizzes':closed_quizzes})

def quiz(request,quiz_id):
    quiz = Quiz.objects.get(id = quiz_id)
    if quiz.result_set.filter(student_email = request.user.email).exists():
        return render(request,'student/student-result.html',{
            'email':request.user.email,
            'qid':quiz_id,
            'result': quiz.result_set.get(student_email = request.user.email).student_marks,
            'total': quiz.result_set.get(student_email = request.user.email).total_marks,
            })
    else: 
        if (quiz.result_set.filter(student_email = request.user.email).exists() or quiz.quiz_end < datetime.now().date()):
            return render(request,'student/student-result.html',{
            'result': -1,
            'total': 0,
            'email':request.user.email,
            'qid':quiz_id,
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
   
    x=quiz.result_set.create(student_email=request.user.email,student_marks=str(results),student_name=request.POST['name'],student_sap=request.POST['sap'],quiz=quiz_id,total_marks=str(total))
    x.save()

    return render(request,'student/results.html',{'result':results,'sap':request.POST['sap'],'total':total,'qid':quiz_id,'email':request.user.email})


def records(request,quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    records = quiz.result_set.all()
    return render(request,'student/records.html',{'quiz_id':quiz_id,'records':records})    

def UserRecords(request):
    record_list = Result.objects.filter(student_email = request.user.email)
    return render(request,'student/student-records.html',{'records':record_list})    