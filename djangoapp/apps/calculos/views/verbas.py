from django.views.generic import ListView

from apps.calculos.models import Calculos, VerbasCalc
# Create your views here.


class ListVerbas(ListView):
    template_name='calculos/listagem_verbas.html'
    model = VerbasCalc

    def get_title(self):
        calculo = Calculos.objects.get(id=self.kwargs['calculo_id'])
        return 'Resumo do Calculo nº {} do Processo {}.'.format(calculo.id, calculo.processo)

    def get_queryset(self):
        self.queryset = self.model.objects.filter(calculo_id=self.kwargs['calculo_id'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Calculo',
                'url': '',
                'activate': None
            },{
                'title': 'Resumo',
                'url': '',
                'activate': 'true'
            }
        ]
        context['calculo'] = Calculos.objects.get(id=self.kwargs['calculo_id'])    
        context['title'] = self.get_title()
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos as verbas cadastrados.'
        
        return context