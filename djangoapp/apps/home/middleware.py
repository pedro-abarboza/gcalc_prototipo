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
                    'title': 'Serviços',
                    'color': '#ffb848',
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
                    'title': 'Calculos',
                    'icon': 'mdi mdi-calculator',
                    'color': '#da542e',
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
                },
            ]
        )
