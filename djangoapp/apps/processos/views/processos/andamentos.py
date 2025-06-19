from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView

from apps.processos.models import Processos, Andamentos
from apps.processos.mixins.andamentos import AndamentosMixin


class ListAndamentos(ListView, AndamentosMixin):
    template_name='processos/listagem_andamentos.html'
    model = Andamentos

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Processos',
                'url': 'listagem_processos',
                'activate': None
            },{
                'title': 'Andamentos',
                'url': '',
                'activate': 'true'
            }
        ]
    
    def get_queryset(self):
        self.queryset = self.model.objects.filter(processo_id=self.kwargs['processo_id'])
        return super().get_queryset()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['processo'] = Processos.objects.get(id=self.kwargs['processo_id'])
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Andamentos do Processo Nº {}'.format(context['processo'])
        
        return context

    def post(self, *args, **kwargs):
        processo = Processos.objects.get(id=self.kwargs['processo_id'])
        self.get_consulta(processo)
        return redirect(reverse('listagem_andamentos', kwargs={'processo_id':processo.id}))