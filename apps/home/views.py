from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name='home/home.html'

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Home',
                'url': 'home',
                'activate': 'true'
            },
        ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        context['title'] = 'Home'
        context['card_title'] = 'Home'
        context['subtitle'] = 'Bem vindo ao G-Calc.'
        context['menu'] = self.menu(self.request)
        
        return context
    
    def menu(self, request):
        
        return[
            {
                'title': 'Processos',
                'permission': request.user.has_perm('processos.view_processos'),
                'color': '#27a9e3',
                'icon': 'mdi mdi-view-list',
                'url': reverse('listagem_processos'),
            },
            {
                'title': 'Calculos',
                'permission': request.user.has_perm('calculos.view_calculos'),
                'icon': 'mdi mdi-calculator',
                'color': '#28b779',
                'url': reverse('listagem_calculos'),
            },
            {
                'title': 'Meus Cálculos',
                'permission': request.user.has_perm('calculos.view_meus_calculos'),
                'icon': 'mdi mdi-file-document-box',
                'color': '#ffb848',
                'url': reverse('listagem_meus_calculos'),
            },
            {
                'title': 'Clientes',
                'permission': request.user.has_perm('clientes.view_clientes'),
                'color': '#2255a4',
                'icon': 'mdi mdi-view-list',
                'url': reverse('listagem_clientes')
            },
            {
                'title': 'Serviços',
                'permission': request.user.has_perm('servicos.view_servicos'),
                'color': '#da542e',
                'icon': 'mdi mdi-wrench',
                'url': reverse('listagem_servicos'),
            },
            {
                'title': 'Meus Serviços',
                'permission': request.user.has_perm('servicos.view_meusservicos'),
                'color': '#27a9e3',
                'icon': 'mdi mdi-view-list',
                'url': reverse('listagem_meus_servicos'),
            },
            {
                'title': 'Acessos',
                'permission': request.user.has_perm('auth.view_user'),
                'color': '#28b779',
                'icon': 'mdi mdi-account-card-details',
                'url': reverse('listagem_usuarios'),
            }
            ]
