from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from .views import *
from django.conf.urls import url

# TEMPLATE TAGGING
app_name = 'student'

urlpatterns = [
    path('', TemplateView.as_view(template_name='college/student/student-homepage.html'), name="homepage"),
    
]
