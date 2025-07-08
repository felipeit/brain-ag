from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rural_producers.models import PropriedadeRural


class ProdutorPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data) -> Response:
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'propriedades': PropriedadeRural.objects.total_fazendas(),
            'hectares': PropriedadeRural.objects.total_hectares(),
            'results': data,
        })
    
class PropriedadePagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data) -> Response:
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'propriedades': PropriedadeRural.objects.total_fazendas(),
            'hectares': PropriedadeRural.objects.total_hectares(),
            'results': data,
        })