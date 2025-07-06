from rest_framework.viewsets import ModelViewSet
from rural_producers.filters import ProdutorFilter
from rural_producers.models import Produtor
from rural_producers.paginations import ProdutorPagination
from rural_producers.serializers import ProdutorSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters.rest_framework import DjangoFilterBackend


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

