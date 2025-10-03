from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView


class SistemaView(TemplateView):
    template_name='sistema/sistema.html'

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Sistema',
                'url': 'sistema',
                'activate': 'true'
            },
        ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Sistema'
        context['card_title'] = 'Sistema'
        context['subtitle'] = 'Bem vindo ao G-Calc.'
        
        return context
