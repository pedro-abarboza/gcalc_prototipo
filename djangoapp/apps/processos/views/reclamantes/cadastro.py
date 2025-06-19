from django.views.generic import CreateView

from apps.processos.models import Reclamantes


class CadReclamantes(CreateView):
    template_name='processos/cadastro.html'
    model = Reclamantes
    fields = '__all__'
     
    
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
                'activate': 'true'
            }
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Reclamantes'
        context['card_title'] = 'Cadastro'
        context['subtitle'] = 'Aqui você cadastra novos Reclamantes.'
        context['form'] = self.get_form()
        
        return context