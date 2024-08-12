from django.contrib import admin
from django.urls import path, include

from .views import QuestionView, Projects

urlpatterns = [
    path('', QuestionView.as_view(), name='question_form'),
    path('projekty', Projects.as_view(), name='projekty')
]