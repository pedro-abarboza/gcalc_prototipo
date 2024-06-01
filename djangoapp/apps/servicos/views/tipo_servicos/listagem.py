from django.views.generic import ListView

from apps.servicos.models import TipoServico


class ListagemTipoServicos(ListView):
    template_name='servicos/tipo_servicos/listagem.html'
    model = TipoServico

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
                'title': 'Tipo de Serviços',
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
        context['title'] = 'Tipos de Serviços'
        context['card_title'] = 'Listagem'
        context['subtitle'] = 'Aqui você tem a lista de todos os Tipos Serviços cadastrados.'
        
        return context