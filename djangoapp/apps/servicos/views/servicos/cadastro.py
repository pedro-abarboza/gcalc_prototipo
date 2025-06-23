import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.contrib import messages

from apps.servicos.models import Servicos
from apps.clientes.models import Clientes
from apps.processos.models import Processos


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
        context['clientes'] = Clientes.objects.all()
        return context
    
    def get_form_kwargs(self):
        kwargs = super(CadServicos, self).get_form_kwargs()

        if self.request.method in ('POST', 'PUT'):
            data = self.request.POST.copy()

            processo, create = Processos.objects.get_or_create(n_processo=data['processo'])
            cliente = Clientes.objects.get(id=data['cliente'])
            tipo_servico = cliente.tiposervicos_set.get(id=data['tipo_servico'])
            data['cliente'] = cliente.nome
            data['tipo_servico'] = tipo_servico.descricao
            data['valor'] = tipo_servico.valor
            data['status'] = 'Pendente'
            kwargs.update({'data': data})

        return kwargs
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Serviço. {}".format(form.errors))
        return HttpResponseRedirect(self.get_success_url())
        
    def form_valid(self, form):
        messages.success(self.request, "Serviço salvo com sucesso")
        return super().form_valid(form)


class SelectTipoServicos(View):

    def get(self, *args, **kwargs):
        result = list(Clientes.objects.filter(id = kwargs['cliente_id']).tiposervicos_set.all().values_list('id', 'descricao'))
        
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')
    
    