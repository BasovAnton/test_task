"""test_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.IndexView.as_view()),
    path("api/v1/newtask/", views.UserTaskCreateAPIView.as_view()),
    path("api/v1/task/<int:pk>/", views.UserTaskUpdateDestroyAPIView.as_view()),
    path("api/v1/user_tasks/", views.UserTasksListAPIView.as_view()),
    path("api/v1/public/", views.PublicTaskListAPIView.as_view()),
]
