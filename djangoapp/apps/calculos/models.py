from django.db import models
from apps.processos.models import Processos


class Calculos(models.Model):

    processo = models.ForeignKey(
        Processos, verbose_name="Nº Processo", on_delete=models.CASCADE
    )
    dt_inicio_calc = models.DateField(
        "D.Inicio", auto_now=False, auto_now_add=False)
    dt_fim_calc = models.DateField(
        "D.Fim", auto_now=False, auto_now_add=False)
    dt_liquidacao = models.DateField(
        "D.Liquidação", auto_now=False, auto_now_add=False)
    dt_criacao = models.DateField(
        "D.Criação", auto_now=True)
    n_arquivo = models.CharField("Nome do aquivo", max_length=200)
    n_pje = models.IntegerField("N.Cálculo")
    per_parcelas_rt = models.FloatField("% Parcelas Remuneratórias e Tributáveis")
    

    class Meta:
        verbose_name = "Cálculo"
        verbose_name_plural = "Cálculos"

    def __str__(self):
        return self.processo.n_processo
    
    @property
    def total_devido(self):
        return self.verbascalc_set.get(descricao='Total').v_devido
    
    @property
    def total_pago(self):
        return self.verbascalc_set.get(descricao='Total').v_pago
    
    @property
    def total_calculado(self):
        return self.verbascalc_set.get(descricao='Total').v_calculado
    
    @property
    def total_juros(self):
        return self.verbascalc_set.get(descricao='Total').juros
    
    @property
    def total_corrigido(self):
        return self.verbascalc_set.get(descricao='Total').v_corrigido
    
    @property
    def total(self):
        return self.verbascalc_set.get(descricao='Total').total
    
    @property
    def get_dt_liquidacao(self):
        from datetime import datetime
        return datetime.strftime(self.dt_liquidacao, "%d/%m/%Y")
    
    @property
    def reclamada(self):
        return self.processo.reclamada.nome
    
    @property
    def reclamante(self):
        return self.processo.reclamante.nome
    
    @property
    def get_processo(self):
        return self.processo.n_processo
    
    def get_coluna(self, descricao):
        verba = self.verbascalc_set.filter(descricao=descricao)
        return verba[0].total if verba else ""


class VerbasCalc(models.Model):

    calculo = models.ForeignKey(Calculos, verbose_name = "Cálculo", on_delete=models.CASCADE)
    descricao = models.CharField("Descrição", max_length=200)
    v_devido = models.FloatField("Valor Devido", null=True, blank=True)
    v_pago = models.FloatField("Valor Pago", null=True, blank=True)
    v_calculado = models.FloatField("Valor Calculado", null=True, blank=True)
    v_corrigido = models.FloatField("Valor Corrigido")
    juros = models.FloatField("Juros")
    total = models.FloatField("Total")
    
    comentario = models.CharField("Comentário", max_length=200, blank=True, null=True)
    insidencia = models.CharField("Incidência(s)", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Verba"
        verbose_name_plural = "Verbas"

    def __str__(self):
        return self.descricao
    
    
class VerbasCalcDetalhes(models.Model):

    verba = models.ForeignKey(VerbasCalc, verbose_name = "Verba", on_delete=models.CASCADE)
    data = models.DateField('Período Mensal', auto_now=False)
    base = models.FloatField('Base', null=True, blank=True)
    divisor = models.FloatField('Divisor', null=True, blank=True)
    multiplicador = models.FloatField('Multiplicador', null=True, blank=True)
    quantidade = models.FloatField('Quantidade', null=True, blank=True)
    dobra = models.BooleanField('Dobra', default=False)
    devido = models.FloatField('Devido')
    pago = models.FloatField('Pago')
    diferenca = models.FloatField('Diferença')
    icm = models.FloatField('Índice Correção')
    v_corrigido = models.FloatField('Valor Corrigido')

    class Meta:
        verbose_name = "Detalhe de Verba"
        verbose_name_plural = "Detalhes de Verbas"

    def __str__(self):
        return self.verba
    

class DebitosReclamado(models.Model):

    calculo = models.ForeignKey(Calculos, verbose_name = "Cálculo", on_delete=models.CASCADE)
    descricao = models.CharField("Descrição", max_length=200)
    valor = models.FloatField("Valor")

    class Meta:
        verbose_name = "Debito"
        verbose_name_plural = "Debitos"

    def __str__(self):
        return self.descricao


class CredDesReclamante(models.Model):

    calculo = models.ForeignKey(Calculos, verbose_name = "Cálculo", on_delete=models.CASCADE)
    descricao = models.CharField("Descrição", max_length=200)
    valor = models.FloatField("Valor")

    class Meta:
        verbose_name = "Crédito e Desconto de Reclamante"
        verbose_name_plural = "Créditos e Descontos de Reclamante"

    def __str__(self):
        return self.descricao
