from django.views.generic import ListView

from apps.calculos.models import Calculos
from apps.processos.models import Processos
# Create your views here.


class ListagemCalculos(ListView):
    template_name='calculos/listagem.html'
    model = Calculos

    def get_title(self):
        complemento = ''
        if 'processo_id' in self.kwargs:
            processo = Processos.objects.get(id=self.kwargs['processo_id'])
            complemento = ' do Processo nº {}'.format(processo)
        return 'Calculos' + complemento

    def get_queryset(self):
        if 'processo_id' in self.kwargs:
            self.queryset = self.model.objects.filter(processo_id=self.kwargs['processo_id'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Processo',
                'url': 'listagem_processos',
                'activate': None
            },{
                'title': 'Calculo',
                'url': '',
                'activate': 'true'
            }
        ]

        if 'processo_id' in self.kwargs:
            context['processo'] = Processos.objects.get(id=self.kwargs['processo_id'])

        context['title'] = self.get_title()
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os calculos cadastrados.'
        
        return context

