from django.contrib import admin

from qualificacao.models.cadastro_obras import CadastroObras
from qualificacao.models.obras_usuarios import ObrasUsuario


class CadastroObrasAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid', )
    list_display = [field.name for field in CadastroObras._meta.fields]


class ObrasUsuarioAdmin(admin.ModelAdmin):

    readonly_fields = ['uuid']
    list_display = [field.name for field in ObrasUsuario._meta.fields]


admin.site.register(CadastroObras, CadastroObrasAdmin)
admin.site.register(ObrasUsuario, ObrasUsuarioAdmin)
