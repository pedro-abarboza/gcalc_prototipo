from django.views.generic import ListView

from apps.servicos.models import Servicos


class ListServicos(ListView):
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
    
    def get_tite(self):
        return 'Serviços'

    def get_subtitle(self):
        return 'Aqui você tem a lista de todos os Serviços cadastrados.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = self.get_tite()
        context['card_title'] = 'Listagem'
        context['subtitle'] = self.get_subtitle()
        
        return context
    
    
class ListMeusServicos(ListServicos):
    template_name='servicos/listagem.html'
    model = Servicos

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Meus Serviços',
                'url': '',
                'activate': None
            },{
                'title': 'Listagem',
                'url': '',
                'activate': 'true'
            }
        ]
    def get_tite(self):
        return 'Meus Serviços'
    
    def get_subtitle(self):
        return 'Aqui você tem a lista de todos os seus Serviços.'
    
    def get_queryset(self):
        self.queryset = Servicos.objects.filter(responsavel=self.request.user)
        return super().get_queryset()