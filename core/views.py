from django.views.generic import TemplateView, UpdateView

class HomeView(TemplateView):
    template_name = 'core/home.html'

