from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class MenuMiddleware(MiddlewareMixin):

    def process_request(self, request):

        setattr(request,
            'menu',
            [
                {
                    'title': 'Home',
                    'icon': 'mdi mdi-home-variant',
                    'color': '#27a9e3',
                    'url': reverse('home'),
                    'url_home': reverse('home'),
                },{
                    'title': 'Processos',
                    'color': '#28b779',
                    'icon': 'mdi mdi-view-list',
                    'url': '',
                    'url_home': reverse('listagem_processos'),
                    'submenu':[
                        {
                            'title': 'Cadastro',
                            'icon': 'mdi mdi-file-outline',
                            'url': reverse('cadastro_processos'),
                        },{
                            'title': 'Listagem',
                            'icon': 'mdi mdi-view-list',
                            'url': reverse('listagem_processos'),
                        },
                    ]
                },{
                    'title': 'Calculos',
                    'icon': 'mdi mdi-calculator',
                    'color': '#ffb848',
                    'url': '',
                    'url_home': reverse('listagem_calculos'),
                    'submenu':[
                        {
                            'title': 'Listagem',
                            'icon': 'mdi mdi-view-list',
                            'url': reverse('listagem_calculos'),
                        },{
                            'title': 'Relatório',
                            'icon': 'mdi mdi-file-document-box',
                            'url': reverse('relatorio_calculos'),
                        },{
                            'title': 'Import PJE-Calc',
                            'icon': 'mdi mdi-cloud-upload',
                            'url': reverse('pjecalc_upload'),
                        },
                    ]
                },{
                    'title': 'Clientes',
                    'color': '#da542e',
                    'icon': 'mdi mdi-view-list',
                    'url': '',
                    'url_home': reverse('listagem_clientes'),
                    'submenu':[
                        {
                            'title': 'Cadastro',
                            'icon': 'mdi mdi-file-outline',
                            'url': reverse('cadastro_clientes'),
                        },{
                            'title': 'Listagem',
                            'icon': 'mdi mdi-view-list',
                            'url': reverse('listagem_clientes'),
                        },
                    ]
                },{
                    'title': 'Serviços',
                    'color': '#2255a4',
                    'icon': 'mdi mdi-wrench',
                    'url': '',
                    'url_home': '',
                    'submenu':[
                        {
                            'title': 'Cadastro',
                            'icon': 'mdi mdi-view-list',
                            'url': reverse('cadastro_servicos'),
                        },{
                            'title': 'Listagem',
                            'icon': 'mdi mdi-view-list',
                            'url': reverse('listagem_servicos'),
                        },{
                            'title': 'Tipos de Servico',
                            'icon': 'mdi mdi-adjust',
                            'url': '',
                            'submenu':[
                                {
                                    'title': 'Cadastro',
                                    'icon': 'mdi mdi-file-outline',
                                    'url': reverse('cadastro_tipo_servicos'),
                                },{
                                    'title': 'Listagem',
                                    'icon': 'mdi mdi-view-list',
                                    'url': reverse('listagem_tipo_servicos'),
                                }
                            ]
                        }
                    ]
                },{
                    'title': 'Acesso',
                    'color': '#da542e',
                    'icon': 'mdi mdi-account-card-details',
                    'url': '',
                    'url_home': '',
                    'submenu':[
                        {
                            'title': 'Usuarios',
                            'icon': 'mdi mdi-account',
                            'url': reverse('listagem_usuarios'),
                        },{
                            'title': 'Grupos',
                            'icon': 'mdi mdi-account-multiple',
                            'url': '',
                            'submenu':[
                                {
                                    'title': 'Cadastro',
                                    'icon': 'mdi mdi-file-outline',
                                    'url': reverse('cadastro_grupos'),
                                },{
                                    'title': 'Listagem',
                                    'icon': 'mdi mdi-view-list',
                                    'url': reverse('listagem_grupos'),
                                },
                            ]
                        },
                    ]
                },
            ]
        )
