from django.contrib import admin
from student.models import Quiz,Question,Choice,Result

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display=('quiz_subject','quiz_name','quiz_end')


admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Result)