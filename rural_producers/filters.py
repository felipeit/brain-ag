from django_filters import rest_framework as filters

from rural_producers.models import Produtor
from rural_producers.models.propriedade_rural import PropriedadeRural


class ProdutorFilter(filters.FilterSet):
    class Meta:
        model = Produtor
        fields = '__all__'



class PropriedadeFilter(filters.FilterSet):
    class Meta:
        model = PropriedadeRural
        fields = '__all__'