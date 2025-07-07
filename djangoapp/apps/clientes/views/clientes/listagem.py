import json
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from apps.clientes.models import Clientes


class ListagemClientes(ListView):
    template_name='clientes/listagem.html'
    model = Clientes

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Clientes',
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
        context['title'] = 'Clientes'
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os Clientes cadastrados.'
        
        return context

class AutoCompClientes(View):

    def get(self, *args, **kwargs):
        text = self.request.GET['term']
        result = list(Clientes.objects.filter(nome__icontains=text).values_list('nome',flat=True))
        data = json.dumps(result)
        return HttpResponse(data, 'application/json')