from django.views import View
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import TemplateView
from test_task import local_settings
# from . import filters
from django.shortcuts import render


from Models.models import Task
# from . import serializers


class IndexView(TemplateView):
    template_name = "API/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_version"] = local_settings.SERVER_VERSION

        return context
