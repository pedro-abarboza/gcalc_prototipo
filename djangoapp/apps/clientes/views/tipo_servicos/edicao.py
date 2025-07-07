import json
import re

from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import UpdateView
from decimal import Decimal
from apps.clientes.models import TipoServicos


class EdiTipoServicosCliente(UpdateView):
    template_name='clientes/tipo_servicos/form.html'
    model = TipoServicos
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('listagem_clientes')
    
    def get_object(self, queryset = None):
        if 'pk' in self.request.POST and self.request.POST['pk']:
            self.kwargs['pk'] = self.request.POST['pk']
        return super().get_object(queryset)
    
    def get_form_kwargs(self):
        kwargs = super(EdiTipoServicosCliente, self).get_form_kwargs()
        if self.request.method == 'POST':
            data = self.request.POST.copy()
            if data['valor']:
                data['valor'] = float(re.sub(r'[^\d,.-]', '', data['valor']).replace('.','').replace(',','.'))
            else:
                data['valor'] = None
            kwargs.update({'data':data})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_title'] = 'Edição de Cliente'
        context['subtitle'] = 'Aqui você edita os dados do {}.'.format(self.object.descricao)
        context['subtitle_list'] = 'Aqui visualiza os Tipos de Serviços cadastrados para {}.'.format(self.object.descricao)
        context['form'] = self.get_form()
        
        return context
    
    def form_invalid(self, form):
        result = {'result': 'error', 'message':"Erro no salvamento do Tipo de Serviço. {}".format(form.errors)}
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')
        
    def form_valid(self, form):
        self.object = form.save()
        result = {'result': 'success', 'message':"Tipo de Serviço salvo com sucesso"}
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')
    
    