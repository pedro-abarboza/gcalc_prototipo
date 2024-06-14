from django.db import models


class Clientes(models.Model):

    nome = models.CharField("Nome", max_length=200)
    cpf = models.IntegerField("CPF", null=True, blank=True, )
    cnpj = models.IntegerField("CNPJ", null=True, blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome
