from rest_framework import viewsets

from ..serializers.fornecedor_obra import FornecedorObraSerializer
from ..models.fornecedor_obra import FornecedorObras

class FornecedorObraViewSet(viewsets.ModelViewSet):
    queryset = FornecedorObras.objects.all()
    serializer_class = FornecedorObraSerializer
    lookup_field = 'uuid'