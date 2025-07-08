from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rural_producers.application.create_produtor_usecase import CreateProdutorUsecase
from rural_producers.application.dto.produtor import ProdutorDTO
from rural_producers.application.update_produtor_usecase import UpdateProdutorUsecase
from rural_producers.infra.api.filters import ProdutorFilter, PropriedadeFilter
from rural_producers.infra.repository.produtor_repository import ProdutorRepository
from rural_producers.models import Produtor, PropriedadeRural
from rural_producers.infra.api.paginations import ProdutorPagination, PropriedadePagination
from rural_producers.infra.api.serializers import ProdutorSerializer, PropriedadeRuralSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status
from rest_framework.response import Response


@extend_schema_view(
    create=extend_schema(tags=['Produtor'], 
                         request=ProdutorSerializer, 
                         responses={201:ProdutorSerializer},
                         description="Cria um produtor junto com as suas propriedades, culturas e safras."
                         ),
    retrieve=extend_schema(tags=['Produtor'],
                               request=ProdutorSerializer, 
                         responses={201:ProdutorSerializer},
                         description="Detalha um produtor junto com as suas propriedades, culturas e safras."
                         ),
    update=extend_schema(tags=['Produtor'],
                             request=ProdutorSerializer, 
                         responses={200:ProdutorSerializer},
                         description="Atualiza um produtor junto com as suas propriedades, culturas e safras."
                         ),
    partial_update=extend_schema(tags=['Produtor'],
                                     request=ProdutorSerializer, 
                         responses={200:ProdutorSerializer},
                         description="Atualiza uma parte do produtor junto com as suas propriedades, culturas e safras."
                         ),
    list=extend_schema(tags=['Produtor'],
                           request=ProdutorSerializer, 
                         responses={200:ProdutorSerializer(many=True)},
                         description="Lista os produtores junto com as suas propriedades, culturas e safras"
                         ),
    destroy=extend_schema(tags=['Produtor'],
                        request=ProdutorSerializer, 
                         responses={204:None},
                         description="Deleta um produtor junto com as suas propriedades, culturas e safras."
                         )
)
class ProdutorViewSet(ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProdutorFilter
    pagination_class = ProdutorPagination

    def create(self, request, *args, **kwargs) -> Response:
        repository = ProdutorRepository(db=Produtor)
        input = ProdutorDTO(**request.data)
        usecase = CreateProdutorUsecase(repo=repository)
        output = usecase.execute(input=input)
        if output.status == status.HTTP_201_CREATED:
            return Response({"message": "Produtor criado com sucesso", "id": output.id}, status=status.HTTP_201_CREATED)
        return Response({"message": "Falha ao criar Produtor", "error": output.error}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs) -> Response:
        produtor_id = kwargs.get('pk')
        repository = ProdutorRepository(db=Produtor)
        usecase = UpdateProdutorUsecase(repo=repository)
        output = usecase.execute(id=produtor_id, data=request.data)
        if output.status == status.HTTP_200_OK:
            return Response({"message": "Produtor atualizado com sucesso", "id": output.id}, status=status.HTTP_200_OK)
        return Response({"message": "Falha ao atualizar Produtor", "error": output.error}, status=status.HTTP_400_BAD_REQUEST)
    
    

@extend_schema_view(
    retrieve=extend_schema(tags=['Propriedade'],
                               request=ProdutorSerializer, 
                         responses={201:ProdutorSerializer},
                         description="Detalha um produtor junto com as suas propriedades, culturas e safras."
                         ),

    list=extend_schema(tags=['Propriedade'],
                           request=ProdutorSerializer, 
                         responses={200:ProdutorSerializer(many=True)},
                         description="Lista os produtores junto com as suas propriedades, culturas e safras"
                         )
)
class PropriedadeRuralViewSet(mixins.RetrieveModelMixin,
                              mixins.ListModelMixin, 
                              GenericViewSet):
    queryset = PropriedadeRural.objects.all()
    serializers_class = PropriedadeRuralSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropriedadeFilter
    pagination_class = PropriedadePagination