from django.urls import path

from apps.calculos.views.delecao import DelCalculos
from apps.calculos.views.importacao import UploadPjeCalc
from apps.calculos.views.listagem import ListCalculos, ListCalculosProcesso, ListMeusCalculos
from apps.calculos.views.verbas import ListVerbas
from apps.calculos.views.verbas_detalhes import ListVerbasDetalhes
from apps.calculos.views.relatorio import RelCalculos



urlpatterns = [
    path('pjecalc_upload', UploadPjeCalc.as_view(), name='pjecalc_upload'),

    path('listagem_calculos', ListCalculos.as_view(), name='listagem_calculos'),

    path('listagem_meus_calculos', ListMeusCalculos.as_view(), name='listagem_meus_calculos'),

    path('listagem_calculos_processo', ListCalculosProcesso.as_view(), name='listagem_calculos_processo'),
    path('listagem_calculos_processo/<int:processo_id>', ListCalculosProcesso.as_view(), name='listagem_calculos_processo'),

    path('delecao_calculos/', DelCalculos.as_view(), name='delecao_calculos'),
    path('delecao_calculos/<int:pk>', DelCalculos.as_view(), name='delecao_calculos'),

    path('listagem_verbas', ListVerbas.as_view(), name='listagem_verbas'),
    path('listagem_verbas/<int:calculo_id>', ListVerbas.as_view(), name='listagem_verbas'),

    path('listagem_verbas_detalhes', ListVerbasDetalhes.as_view(), name='listagem_verbas_detalhes'),
    path('listagem_verbas_detalhes/<int:verba_id>', ListVerbasDetalhes.as_view(), name='listagem_verbas_detalhes'),

    path('relatorio_calculos', RelCalculos.as_view(), name='relatorio_calculos'),
]