import uuid
from django.db import models
from rural_producers.managers import PropriedadeRuralManager
from rural_producers.models import Produtor


class PropriedadeRural(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, related_name='propriedades')
    nome_fazenda = models.CharField("Nome da fazenda (propriedade)", max_length=255)
    area_agricultavel = models.DecimalField("Área agricultável (ha)", max_digits=10, decimal_places=2)
    area_vegetacao = models.DecimalField("Área de vegetação (ha)", max_digits=10, decimal_places=2)
    area_total = models.DecimalField("Área total da fazenda (ha)", max_digits=10, decimal_places=2)
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField("Estado", max_length=2)  # Use sigla: SP, MG, etc.
    objects = PropriedadeRuralManager()

    def __str__(self) -> str:
        return f"{self.nome_fazenda} - {self.produtor.nome_produtor}"