from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'user/home.html')

def login(request):
     if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username = email,password = password)
        if user is not None:
            auth.login(request,user)
            if User.objects.get(username=email).is_staff ==True:
                return redirect('admin-dash')
            else :
                return redirect('student-home')    
        else:
            messages.info(request,'**USER NOT FOUND**')  
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
            messages.info(request,'**EMAIL ALREADY EXISTS**')   
            return redirect('quiz-regi') 
        else:
            user = User.objects.create_user(username = email,password = password,email = email,first_name = first_name,last_name = last_name)
            if request.POST['options-outlined'] == "student" :
                 user.save()
                 return redirect('student-home')
            else:
                if request.POST['teacher-code']== "ABCD":
                    user.is_staff= True
                    user.save()
                    return redirect('admin-dash')

                else:
                    messages.info(request,'**Code INCORRECT**')
                    return redirect('quiz-regi')

    else:        
        return render(request,'user/regi.html')
        
def logout(request):
    auth.logout(request)
    return redirect('quiz-home')
