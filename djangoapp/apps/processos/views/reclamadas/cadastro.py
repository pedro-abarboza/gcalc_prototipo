from django.views.generic import CreateView

from apps.processos.models import Reclamadas


class CadReclamada(CreateView):
    template_name='processos/cadastro.html'
    model = Reclamadas
    fields = '__all__'
     
    
    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': '',
                'activate': None
            },{
                'title': 'Processos',
                'url': '',
                'activate': None
            },{
                'title': 'Reclamadas',
                'url': '',
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Reclamadas'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novas Reclamadas.'
        context['form'] = self.get_form()
        
        return context