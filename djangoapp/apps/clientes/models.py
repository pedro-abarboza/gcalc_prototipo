from django.db import models


class Clientes(models.Model):

    nome = models.CharField("Nome", max_length=200)
    cpf = models.CharField("CPF", max_length=11, null=True, blank=True)
    cnpj = models.CharField("CNPJ", max_length=14, null=True, blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome
