import uuid
from django.db import models


class Safra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField("Safra", max_length=20)

    def __str__(self) -> str:
        return f"{self.id} - {self.nome}"