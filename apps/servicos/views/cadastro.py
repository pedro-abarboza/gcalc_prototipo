from datetime import datetime
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.contrib import messages

from apps.servicos.models import Servicos
from apps.clientes.models import Clientes
from apps.processos.models import Processos
from apps.acesso.models import CustomUser


class CadServicos(CreateView):
    template_name='servicos/form.html'
    model = Servicos
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('listagem_servicos')
    
    def get_url_form(self):
        return reverse('cadastro_servicos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Serviços'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novos Serviço.'
        context['form'] = self.get_form()
        context['url_form'] = self.get_url_form()
        context['clientes'] = list(Clientes.objects.all().values_list('id', 'nome'))
        return context
    
    def get_form_kwargs(self):
        kwargs = super(CadServicos, self).get_form_kwargs()

        if self.request.method in ('POST', 'PUT'):
            data = self.request.POST.copy()

            data['processo'], create = Processos.objects.get_or_create(n_processo=data['processo'])
            data['dt_cadastro'] = datetime.now()
            data['cliente'] = Clientes.objects.get(id=data['cliente'])
            data['tipo_servico'] = data['cliente'].tiposervicos_set.get(id=data['tipo_servico'])
            if 'responsavel' in data and data['responsavel']:
                data['responsavel'] = CustomUser.objects.get(slug=data['responsavel'])
            data['status'] = 'Pendente'
            kwargs.update({'data': data})

        return kwargs
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Serviço. {}".format(form.errors))
        return HttpResponseRedirect(self.get_success_url())
        
    def form_valid(self, form):
        messages.success(self.request, "Serviço salvo com sucesso")
        return super().form_valid(form)


class CadMeusServicos(CadServicos):

    def get_success_url(self):
        return reverse('listagem_meus_servicos')
    

class SelectTipoServicos(View):

    def get(self, *args, **kwargs):
        result = list(Clientes.objects.filter(id = kwargs['cliente_id']).tiposervicos_set.all().values_list('id', 'descricao'))
        
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')
    
    