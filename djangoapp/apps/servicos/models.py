from django.db import models
from django.contrib.auth.models import User

from apps.calculos.models import Calculos
from apps.processos.models import Processos
from apps.clientes.models import Clientes, TipoServicos
    

class Servicos(models.Model):

    CHOICES_STATUS = (
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    )

    tipo_servico = models.CharField(
        verbose_name='Tipo de Serviço',
        null=False, blank=False
    )

    valor = models.DecimalField(
        decimal_places=2, max_digits=10,
        verbose_name='Valor',
        null=False, blank=False
    )

    cliente = models.CharField(
        choices=[(c.nome, c.nome) for c in Clientes.objects.all()],
        verbose_name='Cliente',
        null=False, blank=False
    )

    dt_prazo = models.DateField(
        "Prazo", auto_now=False, auto_now_add=False,
        null=False, blank=False)

    processo = models.CharField(
        choices=[(p.n_processo, p.n_processo) for p in Processos.objects.all()],
        verbose_name='Processo',
        null=False, blank=False
    )

    calculo = models.ForeignKey(
        Calculos, on_delete=models.SET_NULL,
        verbose_name='Cálculo',
        null=True, blank=True
    )

    responsavel = models.CharField(
        choices=[(u.username, u.username) for u in User.objects.all()],
        verbose_name='Responsável',
        null=True, blank=True
    )

    status = models.CharField(
        choices=CHOICES_STATUS, 
        verbose_name='Status', max_length=50, 
        null=True, blank=True
    )

    observacao = models.TextField("Observações", 
        null=True, blank=True)


    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return "{self.processo} - {self.tipo_servico}"


class MeusServicos(Servicos):
    
    class Meta:
        verbose_name = "Meu Serviço"
        verbose_name_plural = "Meus Serviços"