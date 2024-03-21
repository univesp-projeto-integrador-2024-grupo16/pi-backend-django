from rest_framework import viewsets
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response

from ..serializers.serializer_fornecedor import FornecedorSerializer
from ..models.cadastro_fornecedores import CadastroFornecedores, EnderecoFornecedor


class FornecedorView(viewsets.ModelViewSet):
    serializer_class = FornecedorSerializer
    #pagination_class =
    lookup_field = 'uuid'
    queryset = CadastroFornecedores.ativos.order_by('razao_social')

    def create(self, request, *args, **kwargs):
        endereco_fornecedor = request.data.pop('endereco_fornecedor')
        fornecedor = request.data

        new_endereco_fornecedor = EnderecoFornecedor.objects.create(**endereco_fornecedor)
        new_endereco_fornecedor.save()
        new_fornecedor = CadastroFornecedores.ativos.create(**fornecedor, endereco_fornecedor=new_endereco_fornecedor)
        new_fornecedor.save()

        serializer = FornecedorSerializer(new_fornecedor)
        return Response(serializer.data)
