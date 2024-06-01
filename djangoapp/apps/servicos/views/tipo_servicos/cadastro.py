import re
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages

from apps.servicos.models import TipoServico


class CadTipoServicos(CreateView):
    template_name='servicos/tipo_servicos/cadastro.html'
    model = TipoServico
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('listagem_tipo_servicos')
    
    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Tipo de Serviços',
                'url': None,
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Tipos de Serviços'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novos Tipos de Serviço.'
        context['form'] = self.get_form()
        
        return context
    
    def get_form_kwargs(self):
        kwargs = super(CadTipoServicos, self).get_form_kwargs()

        if self.request.method in ('POST', 'PUT'):
            data = self.request.POST.copy()
            valor = re.sub(r"[^\d\-,]","",data['valor']).replace(",",".")
            data.pop('valor')
            data.update({'valor': valor})
            kwargs.update({'data': data})

        return kwargs
       
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Tipo de Serviço. {}".format(form.errors))
        return super().form_invalid(form)
        
    def form_valid(self, form):
        messages.success(self.request, "Tipo de Serviço salvo com sucesso")
        return super().form_valid(form)
    
    