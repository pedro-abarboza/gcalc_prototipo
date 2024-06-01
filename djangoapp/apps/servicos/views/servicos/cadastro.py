from typing import Any
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages

from apps.servicos.models import Servicos


class CadServicos(CreateView):
    template_name='servicos/cadastro.html'
    model = Servicos
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('listagem_servicos')
    
    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Serviços',
                'url': '',
                'activate': None
            },{
                'title': 'Cadastro',
                'url': '',
                'activate': 'True'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Tipos de Serviços'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novos Serviço.'
        context['form'] = self.get_form()
        
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Serviço. {}".format(form.errors))
        response = super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Serviço salvo com sucesso")
        return super().form_valid(form)
    
    