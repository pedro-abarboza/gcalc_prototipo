import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView
from django.contrib import messages

from apps.acesso.models import CustomUser
from apps.servicos.models import Servicos
from apps.clientes.models import Clientes
from apps.processos.models import Processos


class EdiServicos(UpdateView):
    template_name='servicos/form.html'
    model = Servicos
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('listagem_servicos')
    
    def get_url_form(self):
        return reverse('edicao_servicos')
    
    def get_object(self, queryset = None):
        if 'pk' in self.request.POST and self.request.POST['pk']:
            self.kwargs['pk'] = self.request.POST['pk']
        return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Serviços'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você edita o Serviço.'
        context['form'] = self.get_form()
        if context['form'].instance.id:
            cliente = Clientes.objects.get(nome = context['form'].instance.cliente)
            context['tipos_servicos'] = list(
                Clientes.objects.get(nome = context['form'].instance.cliente)
                    .tiposervicos_set.all().values_list('id', 'descricao')
                )
            context['responsaveis'] = list(CustomUser.objects\
                .filter(tipos_servicos=context['form'].instance.tipo_servico)
                .values_list('slug', 'nome_completo'))
            
        else:
            context['tipos_servicos'] = []
            context['responsaveis'] = []
        context['url_form'] = self.get_url_form()
        context['clientes'] = list(Clientes.objects.all().values_list('id', 'nome'))
        return context
    
    def get_form_kwargs(self):
        kwargs = super(EdiServicos, self).get_form_kwargs()

        if self.request.method in ('POST', 'PUT'):
            data = self.request.POST.copy()

            data['processo'], create = Processos.objects.get_or_create(n_processo=data['processo'])
            data['cliente'] = Clientes.objects.get(id=data['cliente'])
            data['tipo_servico'] = data['cliente'].tiposervicos_set.get(id=data['tipo_servico'])
            data['responsavel'] = CustomUser.objects.get(slug=data['responsavel'])
            data['dt_cadastro'] = self.object.dt_cadastro
            kwargs.update({'data': data})

        return kwargs
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Serviço. {}".format(form.errors))
        return HttpResponseRedirect(self.get_success_url())
        
    def form_valid(self, form):
        messages.success(self.request, "Serviço salvo com sucesso")
        return super().form_valid(form)
    
    