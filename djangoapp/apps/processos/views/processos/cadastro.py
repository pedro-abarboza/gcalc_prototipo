from typing import Any
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages

from apps.processos.models import Processos, Reclamadas, Reclamantes


class CadProcessos(CreateView):
    template_name='processos/cadastro.html'
    model = Processos
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('listagem_processos')
    
    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Processos',
                'url': 'listagem_processos',
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Processos'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novos processos.'
        context['form'] = self.get_form()
        
        return context
    
    def get_form_kwargs(self):
        kwargs = super(CadProcessos, self).get_form_kwargs()

        if self.request.method in ('POST', 'PUT'):
            data = self.request.POST.copy()

            reclamada, create = Reclamadas.objects.get_or_create(nome=self.request.POST['reclamada'].upper())
            reclamante, create = Reclamantes.objects.get_or_create(nome=self.request.POST['reclamante'].upper())
            
            data.pop('reclamada')
            data.update({'reclamada': reclamada})
            data.pop('reclamante')
            data.update({'reclamante': reclamante})

            kwargs.update({'data': data})

        return kwargs
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro no salvamento do Processo. {}".format(form.errors))
        response = super().form_invalid(form)
        

    def form_valid(self, form):
        messages.success(self.request, "Processo salvo com sucesso")
        return super().form_valid(form)
    
    