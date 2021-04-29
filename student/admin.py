from django.contrib import admin
from student.models import Quiz,Question,Choice,Result

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display=('quiz_subject','quiz_name','quiz_end')

class ResultAdmin(admin.ModelAdmin):
    list_display=('quiz','student_name','student_sap','student_email')

class ChoiceAdmin(admin.ModelAdmin):
    list_display=('question','choice_text','ans')

class QuestionAdmin(admin.ModelAdmin):
    list_display=('quiz','question_text')

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Result,ResultAdmin)