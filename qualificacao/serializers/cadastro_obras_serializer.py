from rest_framework import serializers

from ..models.cadastro_obras import CadastroObras

class CadastroObrasSerializer(serializers.ModelSerializer):

    class Meta:
        model = CadastroObras
        fields = [field.name for field in CadastroObras._meta.fields]
        read_only_field = ['uuid']
