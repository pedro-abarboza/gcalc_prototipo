import json
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from apps.clientes.models import Clientes


class ListTipoServicosCliente(ListView):
    template_name='clientes/tipo_servicos/listagem_cliente.html'
    model = Clientes

    def get_queryset(self):
        return Clientes.objects.get(id=self.kwargs['cliente_id']).tiposervicos_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Serviços'
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os Clientes cadastrados.'
        context['cliente_id'] = self.kwargs['cliente_id']
        
        return context