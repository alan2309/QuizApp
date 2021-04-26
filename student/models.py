from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse



class Quiz(models.Model):
    quiz_subject = models.CharField(max_length=200)
    quiz_name = models.CharField(max_length=200)
    quiz_end = models.DateField()
    quiz_time = models.CharField(max_length = 10)


    def __str__(self):
        return self.quiz_subject
    def get_absolute_url(self):
        return reverse('quizdetail',kwargs={'pk':self.pk})
    


class Question(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=400)

    def __str__(self):
        return self.question_text 
    def get_absolute_url(self):
        return reverse('quizdetail',kwargs={'pk':self.quiz.pk})

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    ans = models.BooleanField(default = False)

    def __str__(self):
        return self.choice_text
    def get_absolute_url(self):
        return reverse('quizdetail',kwargs={'pk':self.question.quiz.pk})        

class Result(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=150)
    student_sap = models.IntegerField()
    student_email=models.CharField(max_length=255)
    student_marks = models.CharField(max_length=150)
    total_marks=models.CharField(max_length=150)


    def __str__(self):
        return self.student_email