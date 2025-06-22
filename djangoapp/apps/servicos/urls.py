from django.urls import path

from apps.servicos.views.servicos.cadastro import CadServicos
from apps.servicos.views.servicos.listagem import ListServicos, ListMeusServicos


urlpatterns = [
    path('listagem_servicos', ListServicos.as_view(), name='listagem_servicos'),
    path('cadastro_servicos', CadServicos.as_view(), name='cadastro_servicos'),
    path('edicao_servicos', CadServicos.as_view(), name='edicao_servicos'),
    path('delecao_servicos', CadServicos.as_view(), name='delecao_servicos'),

    path('listagem_meus_servicos', ListMeusServicos.as_view(), name='listagem_meus_servicos'),

    
]