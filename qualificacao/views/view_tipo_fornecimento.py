from rest_framework import viewsets

#from ..models.tipo_fornecimento import TipoFornecimento
from ..serializers.tipo_fornecimento_serializer import TipoFornecimentoSerializer
from ..serializers.tipo_fornecimento_serializer import TipoFornecimento

class TipoFornecimentoViewSet(viewsets.ModelViewSet):
    queryset = TipoFornecimento.objects.all()
    serializer_class = TipoFornecimentoSerializer
    lookup_field = 'uuid'