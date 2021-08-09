
from django.urls import path, include
from django.views.generic import TemplateView
from .views import Page2


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html',
         extra_context={'title': 'My Title'})),
    path('second', Page2.as_view()),

]
