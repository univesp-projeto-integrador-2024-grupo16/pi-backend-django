from django.db import models

from uuid import uuid4
from datetime import datetime


class QualificacaoDetalhes(models.Model):

    uuid = models.UUIDField(
        primary_key=True,
        null=False,
        blank=False,
        default=uuid4,
        editable=False,
        unique=True
    )
    nf_bms = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
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

        super(QualificacaoDetalhes, self).save(*args, **kwargs)
        