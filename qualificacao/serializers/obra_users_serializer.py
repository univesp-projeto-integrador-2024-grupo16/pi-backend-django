from rest_framework import serializers

from ..models.obras_usuarios import ObrasUsuario
from ..serializers.user_serializer import UserSerializer
from ..serializers.cadastro_obras_serializer import CadastroObrasSerializer


class ObraUsuariosSerializer(serializers.ModelSerializer):

    auth_user = UserSerializer(many=False)
    obras = CadastroObrasSerializer(many=True)
    class Meta:
        model = ObrasUsuario
        fields = [field.name for field in ObrasUsuario._meta.fields]
        fields.append('auth_user')
        fields.append('obras')
        read_only_field = ['uuid']
