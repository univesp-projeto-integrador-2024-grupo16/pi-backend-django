from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


from ..serializers.qualificacao_serializer import QualificacaoSerializer
from ..models.qualificacao import Qualificacao, QualificacaoDetalhes, TipoFornecimento, CadastroObras
from ..models.cadastro_fornecedores import CadastroFornecedores

class QualificacaoViewSet(viewsets.ModelViewSet):
    #queryset = Qualificacao.objects.all()
    serializer_class = QualificacaoSerializer
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['obra','fornecedor']


    def _inject_avaliation_stats(self, response):
        # print(response.data)
        # response.data.append('stats')
        # response.data['stats'] = {
        #     'count': 10
        # }
        # print(response.data)
        pass
    def get_queryset(self):

        if(len(self.request.query_params) == 2):
            return Qualificacao.objects.filter(obra=self.request.query_params.get('obra'))
        else:
            match self.action:
                case 'retrieve':
                    #print(self.kwargs[self.lookup_field])
                    return Qualificacao.objects.filter(uuid=self.kwargs[self.lookup_field])
                case _:

                    return None
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        self._inject_avaliation_stats(response)
        return response

    # def get_queryset(self):
    #     #qs = Qualificacao.objects.filter(obra=self.request.query_params.get('obra')).values('fornecedor__uuid')
    #     print(self.request.query_params)
    #     qs = Qualificacao.objects.filter(obra=self.request.query_params.get('obra'),fornecedor=self.request.query_params.get('fornecedor__uuid'))
    #     #qs = Qualificacao.objects.filter(fornecedor=self.request.query_params.get('fornecedor'))
    #     return qs

    def create(self, request, *args, **kwargs):

        detalhes_qualificacao = request.data.pop('detalhes_qualificacao')
        tipo_fornecimento = request.data.pop('tipo_fornecimento')
        obra = request.data.pop('obra')
        fornecedor = request.data.pop('fornecedor')
        qualificacao = request.data

        new_detalhes_qualificacao = QualificacaoDetalhes.objects.create(**detalhes_qualificacao)
        new_detalhes_qualificacao.save()

        new_qualificacao = Qualificacao.objects.create(**qualificacao,
                                                       tipo_fornecimento=TipoFornecimento.objects.filter(uuid=tipo_fornecimento).first(),
                                                       obra=CadastroObras.objects.filter(uuid=obra).first(),
                                                       fornecedor=CadastroFornecedores.todos.filter(uuid=fornecedor).first(),
                                                       detalhes_qualificacao=new_detalhes_qualificacao
                                                       )
        new_qualificacao.save()

        serializer = QualificacaoSerializer(new_qualificacao)

        return Response(serializer.data)
