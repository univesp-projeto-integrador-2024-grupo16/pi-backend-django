from django.db import models
from .endereco_fornecedor import EnderecoFornecedor

from uuid import uuid4
from datetime import datetime

"""
Classe que representa o fornecedor com relacionamento 1:1 para o endereco do fornecedor
"""


class ForncedoresTodos(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


class FornecedoresDeletados(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deletado=True)


class FornecedoresAtivos(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deletado=False)


class CadastroFornecedores(models.Model):

    ativos = FornecedoresAtivos()
    inativos = FornecedoresDeletados()
    todos = ForncedoresTodos()
    uuid = models.UUIDField(
        primary_key=True,
        null=False,
        blank=False,
        default=uuid4,
        editable=False,
        unique=True
    )
    cnpj = models.CharField(
        max_length=14,
        unique=True,
        blank=False,
        null=False
    )
    razao_social = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    inscricao_estatual = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    inscricao_municipal = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    endereco_fornecedor = models.OneToOneField(
        to=EnderecoFornecedor,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='fornecedor'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    deletado_em = models.DateTimeField(blank=True, null=True, default=None)
    deletado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.razao_social)

    def delete(self, *args, **kwargs):
        if self.deletado:
            models.Model.delete(self)
        else:
            self.deletado = True
            self.deletado_em = datetime.now()
            self.save()

    def save(self, *args, **kwargs):
        if self.deletado:
            self.deletado = True
            self.deletado_em = datetime.now()
        else:
            self.deletado = False
            self.deletado_em = None

        super(CadastroFornecedores, self).save(*args, **kwargs)
