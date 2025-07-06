from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from rural_producers.managers import PropriedadeRuralManager
from rural_producers.models import PropriedadeRural

@receiver(post_save, sender=PropriedadeRural)
@receiver(post_delete, sender=PropriedadeRural)
def limpar_cache_estatisticas(sender, **kwargs) -> None:
    cache.delete(PropriedadeRuralManager.CACHE_KEY_TOTAL_FAZENDAS)
    cache.delete(PropriedadeRuralManager.CACHE_KEY_TOTAL_HECTARES)