from typing import Any
from uuid import UUID
from pydantic import BaseModel
from rural_producers.application.dto.produtor import ProdutorDTO
from rural_producers.domain.cultura import Cultura
from rural_producers.domain.produtor import Produtor
from rural_producers.domain.propriedade_rural import PropriedadeRural
from rural_producers.domain.safra import Safra
from rural_producers.domain.values_objects.documento_identificacao import DocumentoIdentificacao
from rural_producers.domain.values_objects.email import Email
from rural_producers.domain.values_objects.telefone import Telefone
from rural_producers.infra.repository.produtor_repository import ProdutorRepository


class OutputSucess(BaseModel):
    id: UUID
    status: int = 200

class OutputError(BaseModel):
    error: Any
    status: int = 400

class UpdateProdutorUsecase:
    def __init__(self, repo: ProdutorRepository) -> None:
        self._repo = repo

    def execute(self, id: str, data: dict) -> OutputSucess | OutputError:
        try:
            produtor_model = self._repo.get_by_id(id=id)
            current_data = {
                "doc_identificacao": produtor_model.doc_identificacao,
                "nome_produtor": produtor_model.nome_produtor,
                "email": produtor_model.email,
                "telefone": produtor_model.telefone
            }
            updated_data = {**current_data, **data}
            produtor_domain = Produtor(
                    documento=DocumentoIdentificacao(updated_data["doc_identificacao"]),
                    nome=updated_data["nome_produtor"],
                    email=Email(updated_data["email"]),
                    telefone=Telefone(updated_data["telefone"]),
                    propriedades=[]
                )
            produtor_domain.id = produtor_model.id.hex
            self._repo.update(produtor_domain)
            return OutputSucess(id=produtor_domain.id)
        except Exception as err:
            return OutputError(error=str(err))