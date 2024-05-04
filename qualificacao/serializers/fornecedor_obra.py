from rest_framework import serializers

from ..models.fornecedor_obra import FornecedorObras,CadastroFornecedores
from ..serializers.serializer_fornecedor import FornecedorSerializer

class FornecedorObraSerializer(serializers.ModelSerializer):

    #fornecedores = serializers.SerializerMethodField(read_only=True, many=True)
    fornecedores = FornecedorSerializer(many=True,read_only=True)
    lookup_field = 'obra'
    class Meta:
        model = FornecedorObras
        #fields = [field.name for field in FornecedorObras._meta.fields]
        fields = '__all__'
        #fields.append('fornecedores')
        read_only_fields = ['uuid']
        depth = 1
        extra_kwargs = {
            'fornecedores': {
                'validators': []
            }
        }

    def update(self, instance, validated_data):
        #instance.set(self.validated_data)
        fornecedores = validated_data.pop('validated_data')

        if fornecedores is None:
            instance.fornecedores.clear()

        else:
            for fornecedor in fornecedores:
                instance.fornecedores.add(
                    fornecedor
                )
        return instance

