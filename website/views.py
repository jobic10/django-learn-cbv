from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Page2(TemplateView):
    template_name = 'index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Title set in views'
        return context
