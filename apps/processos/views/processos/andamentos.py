import json
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.http import HttpResponse
from django.views import View

from apps.processos.models import Processos, Andamentos
from apps.processos.mixins.andamentos import AndamentosMixin


class ListAndamentos(ListView, AndamentosMixin):
    template_name='processos/listagem_andamentos.html'
    model = Andamentos
    
    def get_queryset(self):
        self.queryset = self.model.objects.filter(processo_id=self.kwargs['processo_id'])
        return super().get_queryset()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['processo'] = Processos.objects.get(id=self.kwargs['processo_id'])
        context['title'] = 'Andamentos do Processo Nº {}'.format(context['processo'])
        
        return context
    

class AtualizarAndamentos(View, AndamentosMixin):

    def get(self, *args, **kwargs):

        try:
            processo = Processos.objects.get(id=self.kwargs['processo_id'])
            self.get_consulta(processo)
            result = {
                'status': 'success',
                'message': 'Andamentos atualizados com sucesso.',
            }
        except Exception as e:
            result = {
                'status': 'error',
                'message': str(e),
            }
        data = json.dumps(result)
        return HttpResponse(data, 'aplication/json')