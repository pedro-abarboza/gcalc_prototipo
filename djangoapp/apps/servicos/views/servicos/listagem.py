from django.views.generic import ListView

from apps.servicos.models import Servicos


class ListagemServicos(ListView):
    template_name='servicos/listagem.html'
    model = Servicos

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Servicos',
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
        context['title'] = 'Serviços'
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os Serviços cadastrados.'
        
        return context