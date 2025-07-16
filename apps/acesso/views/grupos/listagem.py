import json
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView


class ListagemGrupos(ListView):
    template_name='acesso/grupos/listagem.html'
    model = Group
    fields = '__all__'

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Acesso',
                'url': '',
                'activate': None
            },{
                'title': 'Grupos',
                'url': '',
                'activate': None
            },{
                'title': 'Listagem',
                'url': '',
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Grupos'
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os Grupos cadastrados.'
        
        return context