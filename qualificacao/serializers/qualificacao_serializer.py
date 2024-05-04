from rest_framework import serializers

from ..models.qualificacao import Qualificacao

class QualificacaoSerializer(serializers.ModelSerializer):

    #mean = serializers.Field()

    #tipo_fornecimento = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    class Meta:
        model = Qualificacao
        fields = [field.name for field in Qualificacao._meta.fields]

        fields.append('mean')
        read_only_field = ['uuid']
        depth = 1
