import json
import re
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from apps.processos.models import Processos


class ListProcessos(ListView):
    template_name='processos/listagem.html'
    model = Processos

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
                'title': 'Listagem',
                'url': '',
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Processos'
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os processos cadastrados.'
        
        return context

class AutoCompProcessos(View):

    def get(self, *args, **kwargs):
        term_size={
            7: [],
            9: [],
            13: [],
            14: [],
            16: [],
            20: [],
        }

        text = self.request.GET['term']
        size = len(text)
        if size < 7: text = re.sub(r"(\d{7})", r"\1",text)
        elif size < 9: text = re.sub(r"(\d{7})(\d{2})?", r"\1-\2",text)
        elif size < 13: text = re.sub(r"(\d{7})(\d{2})(\d{4})?", r"\1-\2.\3",text)
        elif size < 14: text = re.sub(r"(\d{7})(\d{2})(\d{4})(\d{1})?", r"\1-\2.\3.\4",text)
        elif size < 16: text = re.sub(r"(\d{7})(\d{2})(\d{4})(\d{1})(\d{2})?", r"\1-\2.\3.\4.\5",text)
        elif size < 20: text = re.sub(r"(\d{7})(\d{2})(\d{4})(\d{1})(\d{2})(\d{4})?", r"\1-\2.\3.\4.\5.",text)

        result = list(Processos.objects.filter(n_processo__icontains=text).values_list('n_processo',flat=True))
        data = json.dumps(result)
        return HttpResponse(data, 'application/json')