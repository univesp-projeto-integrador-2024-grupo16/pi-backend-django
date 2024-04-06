from django.contrib import admin

from qualificacao.models.qualificacao import QualificacaoDetalhes
from qualificacao.models.qualificacao import Qualificacao

class CadastroQualificacaoAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid', )
    list_display = [field.name for field in Qualificacao._meta.fields]

class CadastroQualificacaoDetalhesAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid', )
    list_display = [field.name for field in QualificacaoDetalhes._meta.fields]

admin.site.register(Qualificacao, CadastroQualificacaoAdmin)
admin.site.register(QualificacaoDetalhes, CadastroQualificacaoDetalhesAdmin)
