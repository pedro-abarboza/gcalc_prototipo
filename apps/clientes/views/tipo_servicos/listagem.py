import json
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView

from apps.acesso.models import CustomUser
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
        context['subtitle'] = 'Aqui você tem a lista de todos Tipos de Serviços os Clientes cadastrados.'
        context['cliente_id'] = self.kwargs['cliente_id']
        
        return context


class ListTipoServicosClienteJson(View):
    
    def get(self, *args, **kwargs):
        result = [('','-----')]
        result += list(Clientes.objects.get(id = kwargs['cliente_id']).tiposervicos_set.all().values_list('id', 'descricao'))
        return JsonResponse(result, safe=False)


class ListResponsaveisTipoServicosJson(View):
    
    def get(self, *args, **kwargs):
        result = list(CustomUser.objects\
                .filter(tipos_servicos__id=kwargs['tipo_servico_id'])
                .values_list('slug', 'nome_completo'))
        return JsonResponse(result, safe=False)