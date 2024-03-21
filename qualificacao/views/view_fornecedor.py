from rest_framework import viewsets
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response

from ..serializers.serializer_fornecedor import FornecedorSerializer
from ..models.cadastro_fornecedores import CadastroFornecedores

class FornecedorView(viewsets.ModelViewSet):
    serializer_class = FornecedorSerializer
    #pagination_class =
    lookup_field = 'uuid'
    queryset = CadastroFornecedores.ativos.order_by('razao_social')

    def create(self, request, *args, **kwargs):
        endereco_fornecedor = request.data.pop('endereco_fornecedor')
        serializer = self.serializer_class(data=request.data, context={'endereco_fornecedor': endereco_fornecedor})
        serializer.is_valid(raise_exception=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
