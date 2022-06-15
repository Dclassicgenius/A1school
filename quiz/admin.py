
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Question, Result


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'level', 'question', 'marks', 'answer1', 'answer2', 'answer3', 'answer4', 'answer')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user','course', 'level', 'marks', 'date')
    

admin.site.register(Question, QuestionAdmin)
    
admin.site.register(Result, AnswerAdmin)