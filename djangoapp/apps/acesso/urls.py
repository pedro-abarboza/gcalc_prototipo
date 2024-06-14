from django.urls import path

from apps.acesso.views.usuarios.cadastro import CadUsuarios
from apps.acesso.views.usuarios.edicao import EdiUsuarios
from apps.acesso.views.usuarios.listagem import ListagemUsuarios, AutoCompUsuarios
from apps.acesso.views.usuarios.delecao import DelUsuarios

from apps.acesso.views.grupos.cadastro import CadGrupos
from apps.acesso.views.grupos.edicao import EdiGrupos
from apps.acesso.views.grupos.listagem import ListagemGrupos
from apps.acesso.views.grupos.delecao import DelGrupos


urlpatterns = [
    path('listagem_usuarios', ListagemUsuarios.as_view(), name='listagem_usuarios'),
    path('autocomplete_usuarios', AutoCompUsuarios.as_view(), name='autocomplete_usuarios'),
    path('cadastro_usuarios', CadUsuarios.as_view(), name='cadastro_usuarios'),
    path('edicao_usuarios', EdiUsuarios.as_view(), name='edicao_usuarios'),
    path('edicao_usuarios/<int:pk>', EdiUsuarios.as_view(), name='edicao_usuarios'),
    path('delete_usuarios', DelUsuarios.as_view(), name='delete_usuarios'),
    path('delete_usuarios/<int:pk>', DelUsuarios.as_view(), name='delete_usuarios'),

    path('listagem_grupos', ListagemGrupos.as_view(), name='listagem_grupos'),
    path('cadastro_grupos', CadGrupos.as_view(), name='cadastro_grupos'),
    path('edicao_grupos', EdiGrupos.as_view(), name='edicao_grupos'),
    path('edicao_grupos/<int:pk>', EdiGrupos.as_view(), name='edicao_grupos'),
    path('delete_grupos', DelGrupos.as_view(), name='delete_grupos'),
    path('delete_grupos/<int:pk>', DelGrupos.as_view(), name='delete_grupos'),
]