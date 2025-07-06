from rest_framework.routers import DefaultRouter
from rural_producers.views import ProdutorViewSet

router = DefaultRouter()

router.register('produtor', ProdutorViewSet, basename='produtor')