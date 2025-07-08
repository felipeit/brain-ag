import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_cria_produtor_rural(client, produtor_payload) -> None:
    response = client.post("/api/v1/produtor/", data=produtor_payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["message"] == 'Produtor criado com sucesso'

@pytest.mark.django_db
def test_edita_produtor_rural(client, produtor_payload) -> None:
    create = client.post("/api/v1/produtor/", data=produtor_payload, format="json")
    produtor_id = create.data["id"].hex
    update = client.patch(f"/api/v1/produtor/{produtor_id}/", data={"nome_produtor": "João Atualizado"}, format="json")
    assert update.status_code == status.HTTP_200_OK
    assert update.data["id"].hex == produtor_id

@pytest.mark.django_db
def test_deleta_produtor_rural(client, produtor_payload) -> None:
    create = client.post("/api/v1/produtor/", data=produtor_payload, format="json")
    produtor_id = create.data["id"].hex
    delete = client.delete(f"/api/v1/produtor/{produtor_id}/")
    assert delete.status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.django_db
def test_valida_cpf_invalido(client, produtor_payload) -> None:
    produtor_payload["doc_identificacao"] = "123.456.789-00"  # CPF inválido
    response = client.post("/api/v1/produtor/", data=produtor_payload, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data["error"] == "CPF inválido."

@pytest.mark.django_db
def test_valida_area_agricultavel_mais_vegetacao_nao_excede_total(client, produtor_payload) -> None:
    produtor_payload["propriedades"][0]["area_agricultavel"] = 100
    produtor_payload["propriedades"][0]["area_vegetacao"] = 200
    produtor_payload["propriedades"][0]["area_total"] = 250
    response = client.post("/api/v1/produtor/", data=produtor_payload, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_fazenda_com_varias_culturas_por_safra(client, produtor_payload) -> None:
    create = client.post("/api/v1/produtor/", data=produtor_payload, format="json")
    assert create.status_code == status.HTTP_201_CREATED
    produtor_id = create.data["id"].hex
    detail = client.get(f"/api/v1/produtor/{produtor_id}/", format="json")
    culturas = detail.data["propriedades"][0]["culturas"]
    assert len(culturas) == 2

@pytest.mark.django_db
def test_fazenda_pode_ter_zero_ou_mais_culturas(client, produtor_payload) -> None:
    create = client.post("/api/v1/produtor/", data=produtor_payload, format="json")
    assert create.status_code == status.HTTP_201_CREATED
    produtor_id = create.data["id"].hex
    detail = client.get(f"/api/v1/produtor/{produtor_id}/", format="json")
    assert detail.data["propriedades"][1]["culturas"] == []

@pytest.mark.django_db
def test_total_hectares_e_total_fazendas(client, produtor_payload) -> None:
    client.post("/api/v1/produtor/", data=produtor_payload, format="json")
    response = client.get("/api/v1/produtor/", format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["propriedades"] == 2
    assert response.data["hectares"] == pytest.approx(200.5 + 450.0)