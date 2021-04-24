from django.db import models
from django.utils import timezone
import datetime


class Quiz(models.Model):
    quiz_subject = models.CharField(max_length=200)
    quiz_name = models.CharField(max_length=200)
    quiz_end = models.DateField()

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=400)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    ans = models.BooleanField(default = False)

    def __str__(self):
        return self.choice_text        

class Result(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=150)
    student_sap = models.IntegerField()
    student_marks = models.IntegerField()

    def __str__(self):
        return self.student_sap           