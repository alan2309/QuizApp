from django.contrib import admin
from student.models import Quiz,Question,Choice

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display=('quiz_name','quiz_end','quiz_subject')


admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Choice)