

from django import forms

from categories.models import Category, Subcategory
from quiz.models import Question
from ckeditor.widgets import CKEditorWidget


class QuestionForm(forms.ModelForm):
    
    courseID=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="Course Name", to_field_name="id")
    levelID=forms.ModelChoiceField(queryset=Subcategory.objects.all(),empty_label="Level Name", to_field_name="id")
    class Meta:
        content = forms.CharField(widget=CKEditorWidget())
        model = Question
        fields=['marks','question','answer1','answer2','answer3','answer4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }
    
class UpdateQuestionForm(forms.ModelForm):
    

    class Meta:
        model = Question
        fields=['marks','question','answer1','answer2','answer3','answer4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }