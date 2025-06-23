from django.urls import path

from apps.clientes.views.clientes.cadastro import CadClientes
from apps.clientes.views.clientes.edicao import EdiClientes
from apps.clientes.views.clientes.listagem import ListagemClientes, AutoCompClientes
from apps.clientes.views.clientes.delecao import DelClientes

from apps.clientes.views.tipo_servicos.listagem import ListTipoServicosCliente, ListTipoServicosClienteJson
from apps.clientes.views.tipo_servicos.cadastro import CadTipoServicosCliente
from apps.clientes.views.tipo_servicos.edicao import EdiTipoServicosCliente
from apps.clientes.views.tipo_servicos.delecao import DelTipoServicosCliente


urlpatterns = [
    path('listagem_clientes', ListagemClientes.as_view(), name='listagem_clientes'),
    path('autocomplete_clientes', AutoCompClientes.as_view(), name='autocomplete_clientes'),
    path('cadastro_clientes', CadClientes.as_view(), name='cadastro_clientes'),
    path('edicao_clientes', EdiClientes.as_view(), name='edicao_clientes'),
    path('edicao_clientes/<int:pk>', EdiClientes.as_view(), name='edicao_clientes'),
    path('delecao_clientes', DelClientes.as_view(), name='delecao_clientes'),
    path('delecao_clientes/<int:pk>', DelClientes.as_view(), name='delecao_clientes'),

    path('listagem_tipo_servicos_cliente', ListTipoServicosCliente.as_view(), name='listagem_tipo_servicos_cliente'),
    path('listagem_tipo_servicos_cliente/<int:cliente_id>', ListTipoServicosCliente.as_view(), name='listagem_tipo_servicos_cliente'),
    path('listagem_tipo_servicos_cliente_select', ListTipoServicosClienteJson.as_view(), name='listagem_tipo_servicos_cliente_select'),
    path('listagem_tipo_servicos_cliente_select/<int:cliente_id>', ListTipoServicosClienteJson.as_view(), name='listagem_tipo_servicos_cliente_select'),

    path('cadastro_tipo_servicos_cliente', CadTipoServicosCliente.as_view(), name='cadastro_tipo_servicos_cliente'),
    path('cadastro_tipo_servicos_cliente/<int:cliente_id>', CadTipoServicosCliente.as_view(), name='cadastro_tipo_servicos_cliente'),
    path('edicao_tipo_servicos_cliente', EdiTipoServicosCliente.as_view(), name='edicao_tipo_servicos_cliente'),
    path('edicao_tipo_servicos_cliente/<int:pk>', EdiTipoServicosCliente.as_view(), name='edicao_tipo_servicos_cliente'),
    path('delecao_tipo_servicos_cliente', DelTipoServicosCliente.as_view(), name='delecao_tipo_servicos_cliente'),
    path('delecao_tipo_servicos_cliente/<int:pk>', DelTipoServicosCliente.as_view(), name='delecao_tipo_servicos_cliente'),
]