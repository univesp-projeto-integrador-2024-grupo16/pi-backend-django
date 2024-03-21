from django.db import models

from .cadastro_obras import CadastroObras
from .cadastro_fornecedores import CadastroFornecedores

from uuid import uuid4
from datetime import datetime


class FornecedorObras(models.Model):

    uuid = models.UUIDField(
        primary_key=True,
        null=False,
        blank=False,
        default=uuid4,
        editable=False,
        unique=True
    )
    obra = models.ForeignKey(CadastroObras, on_delete=models.RESTRICT, null=True)
    fornecedores = models.ManyToManyField(CadastroFornecedores)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    deletado_em = models.DateTimeField(blank=True, null=True, default=None)
    deletado = models.BooleanField(default=False)

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

        super(FornecedorObras, self).save(*args, **kwargs)