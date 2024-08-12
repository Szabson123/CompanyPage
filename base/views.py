from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy

from .models import Question
from .forms import QuestionForm


class Projects(TemplateView):
    template_name = 'base/company-projects-page.html'
    

class QuestionView(CreateView):
    template_name = 'base/main_page.html'
    model = Question
    form_class = QuestionForm
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)    
        return response



    