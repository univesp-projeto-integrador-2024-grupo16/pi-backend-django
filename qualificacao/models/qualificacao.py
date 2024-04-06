from django.db import models

from .tipo_fornecimento import TipoFornecimento
from .qualificacao_detalhes import QualificacaoDetalhes
from .cadastro_obras import CadastroObras
from .cadastro_fornecedores import CadastroFornecedores

from uuid import uuid4
from datetime import datetime

class Qualificacao(models.Model):

    uuid = models.UUIDField(
        primary_key=True,
        null=False,
        blank=False,
        default=uuid4,
        editable=False,
        unique=True
    )
    tipo_fornecimento = models.ForeignKey(TipoFornecimento, blank=False, null=True, on_delete=models.SET_NULL)
    obra = models.ForeignKey(CadastroObras, blank=False, null=True, on_delete=models.PROTECT)
    fornecedor = models.ForeignKey(CadastroFornecedores, blank=False, null=True, on_delete=models.PROTECT)
    question_1 = models.FloatField(blank=False, null=False, default=-1)
    question_2 = models.FloatField(blank=False, null=False, default=-1)
    question_3 = models.FloatField(blank=False, null=False, default=-1)
    question_4 = models.FloatField(blank=False, null=False, default=-1)
    question_5 = models.FloatField(blank=False, null=False, default=-1)
    question_6 = models.FloatField(blank=False, null=False, default=-1)
    detalhes_qualificacao = models.OneToOneField(
        to=QualificacaoDetalhes,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='detalhes_qualificacao'
    )

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

        super(Qualificacao, self).save(*args, **kwargs)

    @property
    def mean(self):
        count = 0
        mean = 0
        for field in self._meta.fields:
            if "question" in field.name:
                 if self.__getattribute__(field.name) > -1:
                     mean += float(self.__getattribute__(field.name))
                     count += 1


        try:
             return mean/count
        except ZeroDivisionError:
             return None
