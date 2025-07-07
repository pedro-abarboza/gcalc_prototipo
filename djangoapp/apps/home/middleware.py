from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith(reverse('login')):
            return redirect('login')
        response = self.get_response(request)
        return response

class MenuMiddleware(MiddlewareMixin):

    def process_request(self, request):

        setattr(request,
            'menu',
            [
                {
                    'title': 'Home',
                    'permission': True,
                    'icon': 'mdi mdi-home-variant',
                    'color': '#27a9e3',
                    'url': reverse('home'),
                    'url_home': reverse('home'),
                },
                {
                    'title': 'Processos',
                    'permission': request.user.has_perm('processos.view_processos'),
                    'color': '#28b779',
                    'icon': 'mdi mdi-view-list',
                    'url': reverse('listagem_processos'),
                },
                {
                    'title': 'Calculos',
                    'permission': request.user.has_perm('calculos.view_calculos'),
                    'icon': 'mdi mdi-calculator',
                    'color': '#ffb848',
                    'url': '',
                    'url_home': reverse('listagem_calculos'),
                    'submenu':[
                        {
                            'title': 'Relatório',
                            'permission': request.user.has_perm('calculos.view_calculos'),
                            'icon': 'mdi mdi-file-document-box',
                            'url': reverse('relatorio_calculos'),
                        },
                        {
                            'title': 'Import PJE-Calc',
                            'permission': request.user.has_perm('calculos.add_calculos'),
                            'icon': 'mdi mdi-cloud-upload',
                            'url': reverse('pjecalc_upload'),
                        },
                    ]
                },
                {
                    'title': 'Clientes',
                    'permission': request.user.has_perm('clientes.view_clientes'),
                    'color': '#da542e',
                    'icon': 'mdi mdi-view-list',
                    'url': reverse('listagem_clientes')
                },
                {
                    'title': 'Serviços',
                    'permission': request.user.has_perm('servicos.view_servicos') or request.user.has_perm('servicos.view_meusservicos'),
                    'color': '#2255a4',
                    'icon': 'mdi mdi-wrench',
                    'url': '',
                    'url_home': '',
                    'submenu':[
                        {
                            'title': 'Todos Serviços',
                            'permission': request.user.has_perm('servicos.view_servicos'),
                            'icon': 'mdi mdi-view-list',
                            'url': reverse('listagem_servicos'),
                        },
                        {
                            'title': 'Meus Serviços',
                            'permission': request.user.has_perm('servicos.view_meusservicos'),
                            'icon': 'mdi mdi-view-list',
                            'url': reverse('listagem_meus_servicos'),
                        }
                    ]
                },
                {
                    'title': 'Acesso',
                    'permission': request.user.has_perm('auth.view_user') or request.user.has_perm('auth.view_group'),
                    'color': '#da542e',
                    'icon': 'mdi mdi-account-card-details',
                    'url': '',
                    'url_home': '',
                    'submenu':[
                        {
                            'title': 'Usuarios',
                            'permission': request.user.has_perm('auth.view_user'),
                            'icon': 'mdi mdi-account',
                            'url': reverse('listagem_usuarios'),
                        },
                        {
                            'title': 'Grupos',
                            'permission': request.user.has_perm('auth.view_group') or request.user.has_perm('auth.add_group'),
                            'icon': 'mdi mdi-account-multiple',
                            'url': '',
                            'submenu':[
                                {
                                    'title': 'Cadastro',
                                    'permission': request.user.has_perm('auth.add_group'),
                                    'icon': 'mdi mdi-file-outline',
                                    'url': reverse('cadastro_grupos'),
                                },
                                {
                                    'title': 'Listagem',
                                    'permission': request.user.has_perm('auth.view_group'),
                                    'icon': 'mdi mdi-view-list',
                                    'url': reverse('listagem_grupos'),
                                },
                            ]
                        },
                    ]
                },
            ]
        )
