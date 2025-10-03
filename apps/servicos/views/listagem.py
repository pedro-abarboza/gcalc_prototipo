from django.urls import reverse
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
    
    def get_can_change(self):
        return self.request.user.has_perm('processos.change_servicos')
    
    def get_can_delete(self):
        return self.request.user.has_perm('processos.delete_servicos')
    
    def get_edit_url(self):
        return reverse('edicao_servicos')
    
    def get_cad_url(self):
        return reverse('cadastro_servicos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = self.get_tite()
        context['card_title'] = 'Listagem'
        context['subtitle'] = self.get_subtitle()
        context['perms_change'] = self.get_can_change()
        context['perms_delete'] = self.get_can_delete()
        context['url_edit'] = self.get_edit_url()
        context['url_cad'] = self.get_cad_url()
        
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
    
    def get_can_change(self):
        return self.request.user.has_perm('servicos.change_meus_servicos')
    
    def get_can_delete(self):
        return self.request.user.has_perm('servicos.delete_meus_servicos')
    
    def get_edit_url(self):
        return reverse('edicao_meus_servicos')
    
    def get_cad_url(self):
        return reverse('cadastro_meus_servicos')
    

class DistribuicaoServicos(ListServicos):
    template_name='servicos/listagem.html'
    model = Servicos

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': None
            },{
                'title': 'Distribuição de Serviços',
                'url': '',
                'activate': None
            }
        ]
    def get_tite(self):
        return 'Distribuição de Serviços'
    
    def get_subtitle(self):
        return 'Aqui você tem a lista de todos os Serviços que não foram designados a um responsável.'
    
    def get_queryset(self):
        self.queryset = Servicos.objects.filter(status='Pendente', responsavel__isnull=True)
        return super().get_queryset()
    
    def get_can_change(self):
        return self.request.user.has_perm('servicos.change_meus_servicos')
    
    def get_can_delete(self):
        return self.request.user.has_perm('servicos.delete_meus_servicos')
    
    def get_edit_url(self):
        return reverse('edicao_meus_servicos')
    
    def get_cad_url(self):
        return reverse('cadastro_meus_servicos')