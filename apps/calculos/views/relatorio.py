from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from apps.calculos.mixins.relatorio import RelatorioMixin
from apps.calculos.models import Calculos
# Create your views here.


class RelCalculos(ListView, RelatorioMixin):
    template_name='calculos/relatorio.html'
    model = Calculos

    def get_title(self):
        return 'Relatório de Calculos'

    def get_queryset(self):
        if 'processo' in self.request.GET and self.request.GET['processo']:
            self.kwargs['processo__id'] = self.request.GET['processo']
        if 'reclamante' in self.request.GET and self.request.GET['reclamante']:
            self.kwargs['processo__reclamante__id'] = self.request.GET['reclamante']
        if 'reclamada' in self.request.GET and self.request.GET['reclamada']:
            self.kwargs['processo__reclamada__id'] = self.request.GET['reclamada']
        self.queryset = self.model.objects.filter(**self.kwargs)
        return super().get_queryset()
    
    def get(self, request, *args, **kwargs):
        if 'submit' in request.GET and request.GET['submit'] == 'exportar':
            self.object_list = self.get_queryset()
            context = super().get_context_data(**kwargs)
            context = self.get_relatorio(context)
            return self.get_export(context)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Calculos',
                'url': '',
                'activate': None
            },{
                'title': 'Relatório',
                'url': '',
                'activate': 'true'
            }
        ]
        context = self.get_relatorio(context)
        return context

