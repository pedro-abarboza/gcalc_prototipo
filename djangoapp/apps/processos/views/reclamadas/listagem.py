import json
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from apps.processos.models import Reclamadas


class ListReclamadas(ListView):
    template_name='processos/listagem.html'
    model = Reclamadas

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
                'title': 'Reclamadas',
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


class AutoCompReclamadas(View):

    def get(self, *args, **kwargs):
        text = self.request.GET['term']
        result = list(Reclamadas.objects.filter(nome__icontains=text).values_list('nome',flat=True))
        data = json.dumps(result)
        return HttpResponse(data, 'application/json')