from django.db import models

# Create your models here.

class Parametros(models.Model):

    nome_empresa = models.CharField(
        blank=True, null=True
    )
    logo_icon = models.ImageField(upload_to='logo/')
    logo_text = models.ImageField(upload_to='logo/')

    class Meta:
        verbose_name = "Parametro"
        verbose_name_plural = "Parametros"

    def __str__(self):
        return "{self.nome_empresa}"