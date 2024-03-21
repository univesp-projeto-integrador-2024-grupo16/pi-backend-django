from rest_framework import serializers
from qualificacao.models import CadastroFornecedores, EnderecoFornecedor


class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CadastroFornecedores
        fields = [field.name for field in CadastroFornecedores._meta.fields]
        read_only_fields = ['uuid', 'criado_em', 'deletado_em', 'atualizado_em']

    def validate(self, attrs):
        return super().validate(attrs)
