from django import forms

from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'last_name', 'company_name', 'email', 'phone_number', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'info', 'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'class': 'info', 'placeholder': 'Nazwisko'}),
            'company_name': forms.TextInput(attrs={'class': 'info', 'placeholder': 'Nazwa Firmy'}),
            'email': forms.EmailInput(attrs={'class': 'info', 'placeholder': 'E-mail'}),
            'phone_number': forms.TextInput(attrs={'class': 'info', 'placeholder': 'Numer telefonu'}),
            'text': forms.Textarea(attrs={'class': 'info', 'id': 'form_textarea', 'placeholder': 'Wiadomość'}),
        }