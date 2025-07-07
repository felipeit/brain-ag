from typing import Any
import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient:
    return APIClient()

@pytest.fixture
def produtor_payload() -> dict[str, Any]:
    return {
        "doc_identificacao": "709.457.900-40",
        "nome_produtor": "João da Silva",
        "email": "joao@email.com",
        "telefone": "11999999999",
        "propriedades": [
            {
                "nome_fazenda": "Fazenda Primavera",
                "area_agricultavel": 150.5,
                "area_vegetacao": 30.0,
                "area_total": 200.5,
                "cidade": "Limeira",
                "estado": "SP",
                "culturas": [
                    {"nome_cultura": "Soja", "safra": {"nome": "Safra 2023"}},
                    {"nome_cultura": "Milho", "safra": {"nome": "Safra 2024"}},
                ],
            },
            {
                "nome_fazenda": "Fazenda São Jorge",
                "area_agricultavel": 300.0,
                "area_vegetacao": 100.0,
                "area_total": 450.0,
                "cidade": "Ribeirão Preto",
                "estado": "SP",
                "culturas": [],
            },
        ],
    }