from django_filters import rest_framework as filters

from rural_producers.models import Produtor


class ProdutorFilter(filters.FilterSet):
    # date_range  = filters.DateFromToRangeFilter(method='filter_date_range')
    # draft = filters.BooleanFilter(method='filter_vacancy_draft')
    class Meta:
        model = Produtor
        fields = '__all__'
