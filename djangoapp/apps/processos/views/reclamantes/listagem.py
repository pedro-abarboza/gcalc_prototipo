import json
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from apps.processos.models import Reclamantes


class ListagemReclamantes(ListView):
    template_name='processos/listagem.html'
    model = Reclamantes

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Processos',
                'url': '',
                'activate': None
            },{
                'title': 'Reclamantes',
                'url': '',
                'activate': None
            },{
                'title': 'Listagem',
                'url': '',
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Reclamadas'
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todas as reclamadas cadastrados.'
        
        return context


class AutoCompReclamantes(View):

    def get(self, *args, **kwargs):
        text = self.request.GET['term']
        result = list(Reclamantes.objects.filter(nome__icontains=text).values_list('nome',flat=True))
        data = json.dumps(result)
        return HttpResponse(data, 'application/json')