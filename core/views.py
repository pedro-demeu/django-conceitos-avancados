from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class Error404View(TemplateView):
    template_name = '500.html'