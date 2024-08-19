from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from .models import Question
from .forms import QuestionForm


class MainPageView(FormMixin, TemplateView):
    template_name = 'base/company-page2.html'
    form_class = QuestionForm
    success_url = reverse_lazy('main')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProjectsView(TemplateView):
    template_name = 'base/company-projects-page.html'
    
class ContactView(TemplateView):
    template_name = 'base/contact-company-page.html'
    
class PlanView(TemplateView):
    template_name = 'base/plans-tab.html'
    



    