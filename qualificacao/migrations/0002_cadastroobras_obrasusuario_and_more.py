# Generated by Django 5.0.3 on 2024-03-21 15:14

import django.db.models.manager
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualificacao', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroObras',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('cod_erp_obra', models.CharField(max_length=255)),
                ('nome_obra', models.CharField(max_length=255)),
                ('gerente_obra', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('deletado_em', models.DateTimeField(blank=True, default=None, null=True)),
                ('deletado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ObrasUsuario',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterModelManagers(
            name='cadastrofornecedores',
            managers=[
                ('ativos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddIndex(
            model_name='cadastrofornecedores',
            index=models.Index(fields=['uuid'], name='qualificaca_uuid_3120d0_idx'),
        ),
        migrations.AddIndex(
            model_name='cadastrofornecedores',
            index=models.Index(fields=['cnpj'], name='cnpj_index'),
        ),
        migrations.AddIndex(
            model_name='cadastroobras',
            index=models.Index(fields=['uuid'], name='qualificaca_uuid_eab8e9_idx'),
        ),
        migrations.AddIndex(
            model_name='cadastroobras',
            index=models.Index(fields=['nome_obra'], name='nome_obra_index'),
        ),
        migrations.AddField(
            model_name='obrasusuario',
            name='auth_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='obrasusuario',
            name='obras',
            field=models.ManyToManyField(to='qualificacao.cadastroobras'),
        ),
    ]