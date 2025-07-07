from django.db import models
from django.db.models.signals import post_migrate
from apps.calculos.models import Calculos
from apps.processos.models import Processos
from apps.clientes.models import Clientes, TipoServicos
from apps.acesso.models import CustomUser


def usuario_deletado(sender, **kwargs):
    "Retorna/Cria um usuario para substituir usuarios deletados."
    user, create = CustomUser.objects.get_or_create(username='substituto', defaults={'first_name':'Usuário', 'last_name':'Deletado'})
    return user

post_migrate.connect(usuario_deletado)


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