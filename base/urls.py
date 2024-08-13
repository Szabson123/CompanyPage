from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('projekty', ProjectsView.as_view(), name='projekty'),
    path('plany', PlanView.as_view(), name='plany'),
    path('kontakt', ContactView.as_view(), name='kontakt')
]