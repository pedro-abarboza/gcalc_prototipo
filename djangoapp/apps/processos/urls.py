from django.urls import path

from apps.processos.views.processos.listagem import ListagemProcessos
from apps.processos.views.processos.cadastro import CadProcessos
from apps.processos.views.processos.delecao import DelProcessos

from apps.processos.views.reclamadas.listagem import AutoCompReclamadas, ListagemReclamadas
from apps.processos.views.reclamantes.listagem import AutoCompReclamantes, ListagemReclamantes



urlpatterns = [
    path('listagem_processos', ListagemProcessos.as_view(), name='listagem_processos'),
    path('cadastro_processos', CadProcessos.as_view(), name='cadastro_processos'),
    path('delete_processos', DelProcessos.as_view(), name='delete_processos'),
    path('delete_processos/<int:pk>', DelProcessos.as_view(), name='delete_processos'),
    
    path('autocomplete_reclamada', AutoCompReclamadas.as_view(), name='autocomplete_reclamada'),
    path('listagem_reclamada', ListagemReclamadas.as_view(), name='listagem_reclamada'),

    path('autocomplete_reclamante', AutoCompReclamantes.as_view(), name='autocomplete_reclamante'),
    path('listagem_reclamante', ListagemReclamantes.as_view(), name='listagem_reclamante'),
]