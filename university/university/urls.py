"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tempfile import template
from urllib import request
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from univ import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage.html'), name='home'), # new
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('admin/', admin.site.urls),
    path('student/',TemplateView.as_view(template_name='student.html'), name="student"),
    path('student/studentResult/', views.studentResult),
    path('professor/', TemplateView.as_view(template_name='professor.html'), name="professor"),
    path('professor/courses/', views.professorCourses),
    path('professor/students/', views.professorStudents),
    path('administrator/', TemplateView.as_view(template_name='admin.html'), name="admin"),
    path('administrator/f1/', views.f1),
    path('administrator/f2/', views.f2),
    path('administrator/f3/', views.f3),
]
