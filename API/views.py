from django.shortcuts import render
from django.views.generic import TemplateView

class AboutTemplateAPIView(TemplateView):
    template_name = "Templates/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_version"] = local_settings.SERVER_VERSION

        return context
