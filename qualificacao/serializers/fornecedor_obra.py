from rest_framework import serializers

from ..models.fornecedor_obra import FornecedorObras

class FornecedorObraSerializer(serializers.ModelSerializer):

    class Meta:
        model = FornecedorObras
        fields = [field.name for field in FornecedorObras._meta.fields]
        read_only_fields = ['uuid']
        depth = 1
