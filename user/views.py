from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

def home(request):
    return render(request,'user/home.html')

def login(request):
     if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username = email,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('quiz-index')
        else:
            messages.info(request,'**USER NOT FOUND')  
            return redirect('quiz-login')
     else:        
        return render(request,'user/login.html')  

def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email = email).exists():
            messages.info(request,'**Email already exists')   
            return redirect('quiz-regi') 
        else:
            user = User.objects.create_user(username = email,password = password,email = email,first_name = first_name,last_name = last_name)
            user.save()
            return redirect('quiz-index')
    else:        
        return render(request,'user/regi.html')        


def index(request):
    return HttpResponse("HOME PAGE")