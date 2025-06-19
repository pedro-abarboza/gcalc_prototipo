from django.urls import path

from apps.processos.views.processos.listagem import ListProcessos, AutoCompProcessos
from apps.processos.views.processos.cadastro import CadProcessos
from apps.processos.views.processos.delecao import DelProcessos
from apps.processos.views.processos.andamentos import ListAndamentos

from apps.processos.views.reclamadas.listagem import AutoCompReclamadas, ListReclamadas
from apps.processos.views.reclamantes.listagem import AutoCompReclamantes, ListReclamantes



urlpatterns = [
    path('listagem_andamentos/<int:processo_id>', ListAndamentos.as_view(), name='listagem_andamentos'),

    path('listagem_processos', ListProcessos.as_view(), name='listagem_processos'),
    path('cadastro_processos', CadProcessos.as_view(), name='cadastro_processos'),
    path('autocomplete_processos', AutoCompProcessos.as_view(), name='autocomplete_processos'),

    path('delete_processos', DelProcessos.as_view(), name='delete_processos'),
    path('delete_processos/<int:pk>', DelProcessos.as_view(), name='delete_processos'),
    
    path('listagem_reclamadas', ListReclamadas.as_view(), name='listagem_reclamadas'),
    path('autocomplete_reclamadas', AutoCompReclamadas.as_view(), name='autocomplete_reclamadas'),

    path('autocomplete_reclamantes', AutoCompReclamantes.as_view(), name='autocomplete_reclamantes'),
    path('listagem_reclamantes', ListReclamantes.as_view(), name='listagem_reclamantes'),
]