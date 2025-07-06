from django.db import models 
from django.db.models import Sum, Count
from django.core.cache import cache

class PropriedadeRuralManager(models.Manager):
    CACHE_KEY_TOTAL_FAZENDAS = 'total_fazendas_cadastradas'
    CACHE_KEY_TOTAL_HECTARES = 'total_hectares_registrados'
    CACHE_TIMEOUT = 60 * 60  # 1 hora

    def total_fazendas(self):
        total = cache.get(self.CACHE_KEY_TOTAL_FAZENDAS)
        if total is not None:
            return total
        total = self.aggregate(count=Count('id'))['count'] or 0
        cache.set(self.CACHE_KEY_TOTAL_FAZENDAS, total, self.CACHE_TIMEOUT)
        return total

    def total_hectares(self):
        total = cache.get(self.CACHE_KEY_TOTAL_HECTARES)
        if total is not None:
            return total
        total = self.aggregate(sum=Sum('area_total'))['sum'] or 0
        cache.set(self.CACHE_KEY_TOTAL_HECTARES, total, self.CACHE_TIMEOUT)
        return total