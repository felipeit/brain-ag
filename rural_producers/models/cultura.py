import uuid
from django.db import models


class CulturaPlantada(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    safra = models.ForeignKey("Safra", on_delete=models.CASCADE, related_name='safra')
    propriedade_rural = models.ForeignKey("PropriedadeRural", on_delete=models.CASCADE, related_name='culturas')
    nome_cultura = models.CharField("Cultura plantada", max_length=100)

    def __str__(self) -> str:
        return f"{self.nome_cultura} - {self.safra.nome}"