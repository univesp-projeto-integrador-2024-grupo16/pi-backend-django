# Generated by Django 5.0.3 on 2024-04-06 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualificacao', '0006_qualificacaodetalhes_qualificacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualificacao',
            name='fornecedor_obra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='qualificacao.fornecedorobras'),
        ),
    ]