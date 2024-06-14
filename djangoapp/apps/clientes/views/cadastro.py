from typing import Any
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages

from apps.clientes.models import Clientes


class CadClientes(CreateView):
    template_name='clientes/cadastro.html'
    model = Clientes
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('listagem_clientes')
    
    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Clientes',
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
        context['title'] = 'Clientes'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novos Clientes.'
        context['form'] = self.get_form()
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Cliente. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Cliente salvo com sucesso")
        return super().form_valid(form)
    
    