from django.urls import path

from apps.clientes.views.cadastro import CadClientes
from apps.clientes.views.edicao import EdiClientes
from apps.clientes.views.listagem import ListagemClientes, AutoCompClientes
from apps.clientes.views.delecao import DelClientes


urlpatterns = [
    path('listagem_clientes', ListagemClientes.as_view(), name='listagem_clientes'),
    path('autocomplete_clientes', AutoCompClientes.as_view(), name='autocomplete_clientes'),
    path('cadastro_clientes', CadClientes.as_view(), name='cadastro_clientes'),
    path('edicao_clientes', EdiClientes.as_view(), name='edicao_clientes'),
    path('edicao_clientes/<int:pk>', EdiClientes.as_view(), name='edicao_clientes'),
    path('delete_clientes', DelClientes.as_view(), name='delete_clientes'),
    path('delete_clientes/<int:pk>', DelClientes.as_view(), name='delete_clientes'),
]