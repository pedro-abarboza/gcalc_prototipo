from django.views.generic import ListView

from apps.calculos.models import  VerbasCalc, VerbasCalcDetalhes
# Create your views here.


class ListVerbasDetalhes(ListView):
    template_name='calculos/listagem_verbas_detalhes.html'
    model = VerbasCalcDetalhes

    def get_title(self):
        verba = VerbasCalc.objects.get(id=self.kwargs['verba_id'])
        return 'Processo {} - Calculo nº {} - Detalhes - {}'.format(verba.calculo.processo, verba.calculo.id, verba )

    def get_queryset(self):
        self.queryset = self.model.objects.filter(verba_id=self.kwargs['verba_id'])
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
                'url': '',
                'activate': None
            },{
                'title': 'Calculo',
                'url': '',
                'activate': None
            },{
                'title': 'Verbas',
                'url': '',
                'activate': None
            },{
                'title': 'Detalhes',
                'url': '',
                'activate': 'true'
            }
        ]
        context['title'] = self.get_title()
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os calculos detalhados verbas cadastrados.'
        
        return context