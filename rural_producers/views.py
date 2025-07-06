from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rural_producers.filters import ProdutorFilter, PropriedadeFilter
from rural_producers.models import Produtor, PropriedadeRural
from rural_producers.paginations import ProdutorPagination, PropriedadePagination
from rural_producers.serializers import ProdutorSerializer, PropriedadeRuralSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins

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