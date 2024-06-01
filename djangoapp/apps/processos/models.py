from django.db import models


class Reclamadas(models.Model):

    nome = models.CharField("Nome", max_length=100)

    class Meta:
        verbose_name = "Reclamada"
        verbose_name_plural = "Reclamadas"

    def __str__(self):
        return self.nome
    

class Reclamantes(models.Model):

    nome = models.CharField("Nome", max_length=100)

    class Meta:
        verbose_name = "Reclamante"
        verbose_name_plural = "Reclamantes"

    def __str__(self):
        return self.nome
    
    
class Processos(models.Model):

    n_processo = models.CharField("N.Processo", max_length=26)
    reclamada = models.ForeignKey(Reclamadas, verbose_name="Reclamada", on_delete=models.PROTECT)
    reclamante = models.ForeignKey(Reclamantes, verbose_name="Reclamante", on_delete=models.PROTECT)
    dt_ajuizamento = models.DateField(
        "D.Ajuizamento", auto_now=False, auto_now_add=False
    )
    formato = models.CharField("Formato", max_length=50, null=True, blank=True)
    dt_ult_atualizacao = models.DateField(
        "Ultima Atualização", auto_now=False, auto_now_add=False, null=True, blank=True
    )
    dt_ult_verificacao = models.DateField(
        "Ultima Verificação", auto_now=False, auto_now_add=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "Processo"
        verbose_name_plural = "Processos"

    def __str__(self):
        return self.n_processo


class Andamentos(models.Model):

    processo = models.ForeignKey(Processos, verbose_name="Processos", on_delete=models.CASCADE)
    descricao = models.CharField("Formato", max_length=200, null=True, blank=True)
    codigo = models.CharField("Codigo", max_length=50, null=True, blank=True)
    grau = models.CharField("Grau", max_length=50, null=True, blank=True)
    dt_andamento = models.DateField("Data", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Andamento"
        verbose_name_plural = "Andamentos"

    def __str__(self):
        return self.descricao
