from django.urls import path

from apps.servicos.views.cadastro import CadServicos
from apps.servicos.views.edicao import EdiServicos
from apps.servicos.views.delecao import DelServicos
from apps.servicos.views.listagem import ListServicos, ListMeusServicos


urlpatterns = [
    path('listagem_servicos', ListServicos.as_view(), name='listagem_servicos'),
    path('cadastro_servicos', CadServicos.as_view(), name='cadastro_servicos'),

    path('edicao_servicos', EdiServicos.as_view(), name='edicao_servicos'),
    path('edicao_servicos/<int:pk>', EdiServicos.as_view(), name='edicao_servicos'),

    path('delecao_servicos', DelServicos.as_view(), name='delecao_servicos'),
    path('delecao_servicos/<int:pk>', DelServicos.as_view(), name='delecao_servicos'),

    path('listagem_meus_servicos', ListMeusServicos.as_view(), name='listagem_meus_servicos'),
]