from django.urls import path

from apps.calculos.views.delecao import DelCalculos
from apps.calculos.views.importacao import UploadPjeCalc
from apps.calculos.views.listagem import ListagemCalculos
from apps.calculos.views.verbas import ListagemVerbas
from apps.calculos.views.verbas_detalhes import ListagemVerbasDetalhes
from apps.calculos.views.relatorio import RelatorioCalculos



urlpatterns = [
    path('pjecalc_upload', UploadPjeCalc.as_view(), name='pjecalc_upload'),

    path('listagem_calculos', ListagemCalculos.as_view(), name='listagem_calculos'),
    path('listagem_calculos/<int:processo_id>', ListagemCalculos.as_view(), name='listagem_calculos'),

    path('delete_calculos/', DelCalculos.as_view(), name='delete_calculos'),
    path('delete_calculos/<int:pk>', DelCalculos.as_view(), name='delete_calculos'),

    path('listagem_verbas', ListagemVerbas.as_view(), name='listagem_verbas'),
    path('listagem_verbas/<int:calculo_id>', ListagemVerbas.as_view(), name='listagem_verbas'),

    path('listagem_verbas_detalhes', ListagemVerbasDetalhes.as_view(), name='listagem_verbas_detalhes'),
    path('listagem_verbas_detalhes/<int:verba_id>', ListagemVerbasDetalhes.as_view(), name='listagem_verbas_detalhes'),

    path('relatorio_calculos', RelatorioCalculos.as_view(), name='relatorio_calculos'),
]