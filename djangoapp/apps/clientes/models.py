from django.db import models


class Clientes(models.Model):

    nome = models.CharField("Nome", max_length=200)
    cpf = models.IntegerField("CPF", null=True, blank=True)
    cnpj = models.IntegerField("CNPJ", null=True, blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome
    

class TipoServicos(models.Model):

    cliente = models.ForeignKey(
        Clientes, on_delete=models.CASCADE,
        verbose_name='Cliente',
        null=False, blank=False
    )

    descricao = models.CharField(verbose_name="Descrição", max_length=200,
                                 null=False, blank=False)
    valor = models.FloatField(verbose_name="Valor", null=True, blank=True)

    class Meta:
        verbose_name = "Tipo de Serviço"
        verbose_name_plural = "Tipos de Serviço"

    def __str__(self):
        return self.descricao
