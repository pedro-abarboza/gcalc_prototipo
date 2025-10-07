from decimal import Decimal
import json
import re
from typing import Any
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView

from apps.clientes.models import Clientes, TipoServicos


class CadTipoServicosCliente(CreateView):
    template_name='clientes/tipo_servicos/form.html'
    model = TipoServicos
    fields = '__all__'
    
    
    def get_url_form(self):
        return reverse('cadastro_clientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = Clientes.objects.get(id=self.kwargs['cliente_id'])
        context['card_title'] = 'Cadastro de Tipos de Serviços'
        context['subtitle'] = 'Aqui você cadastra Tipos de Serviços prestados para o Cliente - {}.'.format(cliente.nome)
        context['url_form'] = self.get_url_form()
        context['form'] = self.get_form()
        context['cliente_id'] = cliente.id
        return context
    
    def get_form_kwargs(self):
        kwargs = super(CadTipoServicosCliente, self).get_form_kwargs()
        if self.request.method == "POST":
            data = self.request.POST.copy()
            data['valor'] = float(re.sub(r'[^\d,]', '', data['valor']).replace(',', '.'))
            kwargs.update({'data': data})
        return kwargs
    
    def form_invalid(self, form):
        result = {'result': 'error', 'message':"Erro no salvamento do Tipo de Serviço. {}".format(form.errors)}
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')
        
    def form_valid(self, form):
        self.object = form.save()
        result = {'result': 'success', 'message':"Tipo de Serviço salvo com sucesso"}
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')