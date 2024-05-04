from rest_framework import viewsets

from ..models.obras_usuarios import ObrasUsuario
from ..serializers.obra_users_serializer import ObraUsuariosSerializer

class ObrasUserView(viewsets.ModelViewSet):

    serializer_class = ObraUsuariosSerializer

    def get_queryset(self):
        queryset = ObrasUsuario.objects.filter(auth_user=self.request.user.id)
        return queryset
