import json
from django.db.models.base import Model as Model
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import DeleteView
from django.contrib import messages

from apps.clientes.models import TipoServicos


class DelTipoServicosCliente(DeleteView):
    template_name='clientes/tipo_servicos/delecao.html'
    model = TipoServicos

    def get_success_url(self):
        return reverse('listagem_clientes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Deleção de Cliente'
        context['object'] = self.get_object()
        return context
    
    def get_object(self, queryset = None):
        if 'pk' not in self.kwargs:
            self.kwargs['pk'] = self.request.POST['id']
        return super().get_object(queryset)
    
    def form_invalid(self, form):
        result = {'result': 'error', 'message':"Erro na Deleção do Tipo de Serviço. {}".format(form.errors)}
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')
        
    def form_valid(self, form):
        self.object.delete()
        result = {'result': 'success', 'message':"Tipo de Serviço Deletado com sucesso"}
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')
    
    