from django.urls import path

from apps.servicos.views.tipo_servicos.cadastro import CadTipoServicos
from apps.servicos.views.tipo_servicos.edicao import EdiTipoServicos
from apps.servicos.views.tipo_servicos.listagem import ListTipoServicos
from apps.servicos.views.tipo_servicos.delecao import DelTipoServicos

from apps.servicos.views.servicos.cadastro import CadServicos
from apps.servicos.views.servicos.listagem import ListServicos


urlpatterns = [
    path('listagem_servicos', ListServicos.as_view(), name='listagem_servicos'),
    path('cadastro_servicos', CadServicos.as_view(), name='cadastro_servicos'),


    path('listagem_tipo_servicos', ListTipoServicos.as_view(), name='listagem_tipo_servicos'),
    path('cadastro_tipo_servicos', CadTipoServicos.as_view(), name='cadastro_tipo_servicos'),
    path('edicao_tipo_servicos', EdiTipoServicos.as_view(), name='edicao_tipo_servicos'),
    path('edicao_tipo_servicos/<int:pk>', EdiTipoServicos.as_view(), name='edicao_tipo_servicos'),
    path('delete_tipo_servicos', DelTipoServicos.as_view(), name='delete_tipo_servicos'),
    path('delete_tipo_servicos/<int:pk>', DelTipoServicos.as_view(), name='delete_tipo_servicos'),
]