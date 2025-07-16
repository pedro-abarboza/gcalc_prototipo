from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name='home/home.html'

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': 'true'
            },
        ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Home'
        context['card_title'] = 'Home'
        context['subtitle'] = 'Bem vindo ao G-Calc.'
        
        return context
