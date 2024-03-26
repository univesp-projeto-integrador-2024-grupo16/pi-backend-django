from rest_framework import serializers

from ..models.tipo_fornecimento import TipoFornecimento

class TipoFornecimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoFornecimento
        fields = [field.name for field in TipoFornecimento._meta.fields]
        read_only_fields = ['uuid']
