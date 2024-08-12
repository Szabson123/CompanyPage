from django import forms

from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'last_name', 'company_name', 'email', 'phone_number', 'text'] 