from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers.fornecedor_obra import FornecedorObraSerializer
from ..models.fornecedor_obra import FornecedorObras

class FornecedorObraViewSet(viewsets.ModelViewSet):
    #queryset = FornecedorObras.objects.all()
    serializer_class = FornecedorObraSerializer
    lookup_field = 'uuid'


    def get_queryset(self):
        #print(self.request.data == {})
        if self.request.data == {}:
            qs = FornecedorObras.objects.filter(obra=self.request.query_params.get('obra'))
        else:
            qs = FornecedorObras.objects.filter(obra=self.request.data.get('obra'))
        return qs

    def create(self, request, *args, **kwargs):



        obra = self.get_queryset().filter(obra=request.data.get('obra')).first()

        if obra == None:
            return super().create(request, *args, **kwargs)

        else:
            print('Data:  ', request.data)
            serializer = FornecedorObraSerializer(
                instance=obra,
                data=request.data,
                many=False,
                context={'request': request},
                partial=True
            )
            serializer.is_valid(raise_exception=False)
            serializer.save(validated_data=request.data.get('fornecedores'))
            return Response(
                serializer.data
            )
           # print(request.data.get('obra'))
        #print(request.data.get('fornecedores'))
            # print(obra)
            # print(serializer.data)
            # return Response(None)
        # pass



    # def create(self, request, *args, **kwargs):
    #     print('request ',  self.request.data)
    #     obra = self.request.data.pop('obra')
    #     fornecedores = []
    #
    #     if obra not in list(FornecedorObras.objects.filter(obra=obra)):
    #         print(list(FornecedorObras.objects.filter(obra=obra)))
    #         serializer = FornecedorObras.objects.create(obra=obra,fornecedores=self.request.data.pop('fornecedores'))
    #         print('nEw', serializer.data)
    #         return Response(serializer.data)
    #     else:
    #         serializer = self.update(self, request=request, *args, **kwargs)
    #         print('Update', serializer.data)
    #         return Response(serializer.data)
    #
    #

        # print(fornecedores)
        #
        # #serializer = FornecedorObraSerializer(self.request.data)
        # return Response("OK")