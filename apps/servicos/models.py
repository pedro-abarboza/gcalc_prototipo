from django.db import models
from django.db.models.signals import post_migrate
from apps.calculos.models import Calculos
from apps.processos.models import Processos
from apps.clientes.models import Clientes, TipoServicos
from apps.acesso.models import CustomUser, usuario_deletado


class Servicos(models.Model):

    CHOICES_STATUS = (
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    )

    tipo_servico = models.ForeignKey(
        TipoServicos,
        on_delete=models.PROTECT,
        verbose_name='Tipo de Serviço',
        null=False, blank=False
    )

    cliente = models.ForeignKey(
        Clientes,
        on_delete=models.PROTECT,
        verbose_name='Cliente',
        null=False, blank=False
    )

    dt_cadastro = models.DateField(
        "Cadastro", auto_now=False, auto_now_add=False,
        null=False, blank=False)

    dt_prazo = models.DateField(
        "Prazo", auto_now=False, auto_now_add=False,
        null=False, blank=False)
    
    dt_conclusao = models.DateField(
        "conclusao", auto_now=False, auto_now_add=False,
        null=True, blank=True)

    processo = models.ForeignKey(
        Processos,
        on_delete=models.PROTECT,
        verbose_name='Processo',
        null=False, blank=False
    )

    calculo = models.ForeignKey(
        Calculos, on_delete=models.SET_NULL,
        verbose_name='Cálculo',
        null=True, blank=True
    )

    responsavel = models.ForeignKey(
        CustomUser,
        on_delete=models.SET(usuario_deletado),
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


class Faturas(models.Model):

    CHOICES_FATURA = (
        ('Atrasado', 'Atrasado'),
        ('Em Analise', 'Em Analise'),
        ('Enviado', 'Enviado'),
        ('Faturado', 'Faturado'),
        ('Pago', 'Pago'),
    )

    servicos = models.ManyToManyField(Servicos)
    usuario_cadastro = models.ForeignKey(
        CustomUser,
        on_delete=models.SET(usuario_deletado),
        verbose_name='Responsável',
        null=True, blank=True
    )
    dt_cadastro = models.DateField(
        "Cadastro", 
        auto_now_add=True,
        null=False, blank=False)
    dt_faturamento = models.DateField(
        "Faturamento", 
        auto_now=False, auto_now_add=False,
        null=True, blank=True)
    dt_prazo = models.DateField(
        "Prazo", 
        auto_now=False, auto_now_add=False,
        null=True, blank=True)
    status = models.CharField(
        'Status',
        null=True, blank=True,
        choices=CHOICES_FATURA)
    nota_fiscal = models.CharField(
        'Nota Fiscal',
        null=True, blank=True)
    valor_total = models.DecimalField(
        'Total',
        null=True, blank=True,
        max_digits=8,
        decimal_places=2)
    observacoes = models.TextField('Observações')

    class Meta:
        verbose_name = "Fatura"
        verbose_name_plural = "Faturas"