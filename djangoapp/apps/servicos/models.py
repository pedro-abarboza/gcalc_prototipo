from django.db import models

from apps.calculos.models import Calculos
from apps.processos.models import Processos
from apps.clientes.models import Clientes

class TipoServico(models.Model):

    descricao = models.CharField("Nome", max_length=200,
                                 null=False, blank=False)
    valor = models.FloatField("Valor", null=True, blank=True)

    class Meta:
        verbose_name = "Tipo de Serviço"
        verbose_name_plural = "Tipos de Serviço"

    def __str__(self):
        return self.descricao
    

class Servicos(models.Model):

    tipo_servico = models.ForeignKey(
        TipoServico, on_delete=models.DO_NOTHING,
        null=False, blank=False
    )

    cliente = models.ForeignKey(
        Clientes, on_delete=models.DO_NOTHING,
        null=False, blank=False
    )

    processo = models.ForeignKey(
        Processos, on_delete=models.DO_NOTHING,
        null=False, blank=False
    )

    calculo = models.ForeignKey(
        Calculos, on_delete=models.SET_NULL,
        null=True, blank=True
    )

    status = models.CharField(
        'Status', max_length=50, null=True, 
        blank=True
    )

    observacao = models.TextField("Observações")


    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return "{self.processo} - {self.tipo_servico}"
