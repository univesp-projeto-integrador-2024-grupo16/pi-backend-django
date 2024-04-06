# Generated by Django 5.0.3 on 2024-04-06 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualificacao', '0007_qualificacao_fornecedor_obra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualificacao',
            name='fornecedor_obra',
        ),
        migrations.AddField(
            model_name='qualificacao',
            name='fornecedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='qualificacao.cadastrofornecedores'),
        ),
        migrations.AddField(
            model_name='qualificacao',
            name='obra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='qualificacao.cadastroobras'),
        ),
    ]