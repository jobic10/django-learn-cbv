
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html',
         extra_context={'title': 'My Title'})),
]
