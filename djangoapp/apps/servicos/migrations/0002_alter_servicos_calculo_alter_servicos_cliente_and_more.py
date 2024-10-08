# Generated by Django 5.0.6 on 2024-06-01 03:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculos', '0002_remove_verbascalc_quantidade'),
        ('clientes', '0002_alter_clientes_cnpj_alter_clientes_cpf'),
        ('processos', '0006_andamentos_codigo_alter_andamentos_grau'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='calculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calculos.calculos', verbose_name='Cálculo'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.clientes', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='processo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='processos.processos', verbose_name='Processo'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='tipo_servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='servicos.tiposervico', verbose_name='Tipo de Serviço'),
        ),
        migrations.AlterField(
            model_name='tiposervico',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
    ]
