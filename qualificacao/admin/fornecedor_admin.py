from django.contrib import admin

from qualificacao.models.cadastro_fornecedores import CadastroFornecedores, EnderecoFornecedor


class EnderecoFornecedorAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid', )
    list_display = [field.name for field in EnderecoFornecedor._meta.fields]


class CadastroFornecedoresAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid',)
    list_display = [
      field.name for field in CadastroFornecedores._meta.fields
    ]


admin.site.register(EnderecoFornecedor, EnderecoFornecedorAdmin)
admin.site.register(CadastroFornecedores, CadastroFornecedoresAdmin)
