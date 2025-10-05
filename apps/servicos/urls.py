from django.urls import path

from apps.servicos.views.cadastro import CadFatura, CadServicos, CadMeusServicos
from apps.servicos.views.edicao import EdiServicos, EdiMeusServicos
from apps.servicos.views.delecao import DelServicos
from apps.servicos.views.listagem import ListFaturas, ListFiltroServicosJson,\
    ListServicos, ListMeusServicos


urlpatterns = [
    path('listagem_servicos', ListServicos.as_view(), name='listagem_servicos'),
    path('listagem_filtro_servicos', ListFiltroServicosJson.as_view(), name='listagem_filtro_servicos_json'),
    path('cadastro_servicos', CadServicos.as_view(), name='cadastro_servicos'),
    path('cadastro_meus_servicos', CadMeusServicos.as_view(), name='cadastro_meus_servicos'),

    path('edicao_servicos', EdiServicos.as_view(), name='edicao_servicos'),
    path('edicao_servicos/<int:pk>', EdiServicos.as_view(), name='edicao_servicos'),

    path('edicao_meus_servicos', EdiMeusServicos.as_view(), name='edicao_meus_servicos'),
    path('edicao_meus_servicos/<int:pk>', EdiMeusServicos.as_view(), name='edicao_meus_servicos'),

    path('delecao_servicos', DelServicos.as_view(), name='delecao_servicos'),
    path('delecao_servicos/<int:pk>', DelServicos.as_view(), name='delecao_servicos'),

    path('listagem_meus_servicos', ListMeusServicos.as_view(), name='listagem_meus_servicos'),

    path('listagem_faturas', ListFaturas.as_view(), name='listagem_faturas'),
    path('cadastro_faturas', CadFatura.as_view(), name='cadastro_faturas'),
]