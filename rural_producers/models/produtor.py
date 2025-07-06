import uuid
from django.db import models


class Produtor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doc_identificacao = models.CharField("Documento (CPF ou CNPJ)", max_length=18, unique=True)
    nome_produtor = models.CharField("Nome do produtor", max_length=255)
    email = models.EmailField("Email do produtor", max_length=255, blank=True, null=True)
    telefone = models.CharField("Principal Contato do produtor", max_length=255)

    def __str__(self) -> str:
        return f"{self.nome_produtor} - {self.doc_identificacao}"