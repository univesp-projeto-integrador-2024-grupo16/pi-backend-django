from django.contrib import admin

from qualificacao.models.cadastro_fornecedores import CadastroFornecedores, EnderecoFornecedor
from qualificacao.models.fornecedor_obra import FornecedorObras


class EnderecoFornecedorAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid', )
    list_display = [field.name for field in EnderecoFornecedor._meta.fields]


class CadastroFornecedoresAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid',)
    list_display = [
      field.name for field in CadastroFornecedores._meta.fields
    ]


class FornecedorObrasAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = [
      field.name for field in FornecedorObras._meta.fields
    ]


admin.site.register(EnderecoFornecedor, EnderecoFornecedorAdmin)
admin.site.register(CadastroFornecedores, CadastroFornecedoresAdmin)
admin.site.register(FornecedorObras,FornecedorObrasAdmin)
