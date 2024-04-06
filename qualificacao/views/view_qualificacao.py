from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers.qualificacao_serializer import QualificacaoSerializer
from ..models.qualificacao import Qualificacao, QualificacaoDetalhes

class QualificacaoViewSet(viewsets.ModelViewSet):
    queryset = Qualificacao.objects.all()
    serializer_class = QualificacaoSerializer
    lookup_field = 'uuid'

    def create(self, request, *args, **kwargs):
        detalhes_qualificacao = request.data.pop('detalhes_qualificacao')
        qualificacao = request.data

        new_detalhes_qualificacao = QualificacaoDetalhes.create(**detalhes_qualificacao)
        new_detalhes_qualificacao.save()
        new_qualificacao =  Qualificacao.create(**qualificacao,detalhes_qualificacao=new_detalhes_qualificacao)
        new_qualificacao.save()

        serializer = QualificacaoSerializer(new_qualificacao)

        return Response(serializer.data)