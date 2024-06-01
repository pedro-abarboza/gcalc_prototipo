from django.urls import path

from apps.servicos.views.tipo_servicos.cadastro import CadTipoServicos
from apps.servicos.views.tipo_servicos.edicao import EdiTipoServicos
from apps.servicos.views.tipo_servicos.listagem import ListagemTipoServicos
from apps.servicos.views.tipo_servicos.delecao import DelTipoServico

from apps.servicos.views.servicos.cadastro import CadServicos
from apps.servicos.views.servicos.listagem import ListagemServicos


urlpatterns = [
    path('listagem_servicos', ListagemServicos.as_view(), name='listagem_servicos'),
    path('cadastro_servicos', CadServicos.as_view(), name='cadastro_servicos'),


    path('listagem_tipo_servicos', ListagemTipoServicos.as_view(), name='listagem_tipo_servicos'),
    path('cadastro_tipo_servicos', CadTipoServicos.as_view(), name='cadastro_tipo_servicos'),
    path('edicao_tipo_servicos', EdiTipoServicos.as_view(), name='edicao_tipo_servicos'),
    path('edicao_tipo_servicos/<int:pk>', EdiTipoServicos.as_view(), name='edicao_tipo_servicos'),
    path('delete_tipo_servicos', DelTipoServico.as_view(), name='delete_tipo_servicos'),
    path('delete_tipo_servicos/<int:pk>', DelTipoServico.as_view(), name='delete_tipo_servicos'),
]