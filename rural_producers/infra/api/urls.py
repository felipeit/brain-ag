from rest_framework.routers import DefaultRouter
from rural_producers.infra.api.views import ProdutorViewSet, PropriedadeRuralViewSet

router = DefaultRouter()

router.register('produtor', ProdutorViewSet, basename='produtor')
router.register('proriedade', PropriedadeRuralViewSet, basename='propriedade')