from django.db import models

from accounts.models import Account
from categories.models import Category, Subcategory
from ckeditor.fields import RichTextField


class Question(models.Model):
    course=models.ForeignKey(Category,on_delete=models.CASCADE)
    level=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=RichTextField(max_length=600)
    # question=models.TextField(max_length=600)
    answer1=models.CharField(max_length=200)
    answer2=models.CharField(max_length=200)
    answer3=models.CharField(max_length=200)
    answer4=models.CharField(max_length=200)
    cat=(('Answer1','Answer1'),('Answer2','Answer2'),('Answer3','Answer3'),('Answer4','Answer4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    course = models.ForeignKey(Category,on_delete=models.CASCADE)
    level=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
