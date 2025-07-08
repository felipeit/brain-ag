from uuid import UUID
from pydantic import BaseModel
from rural_producers.application.dto.produtor import ProdutorDTO
from rural_producers.domain.cultura import Cultura
from rural_producers.domain.produtor import Produtor
from rural_producers.domain.propriedade_rural import PropriedadeRural
from rural_producers.domain.safra import Safra
from rural_producers.domain.values_objects.telefone import Telefone 
from rural_producers.domain.values_objects.documento_identificacao import DocumentoIdentificacao
from rural_producers.domain.values_objects.email import Email
from rural_producers.infra.repository.produtor_repository import ProdutorRepository

class Output(BaseModel):
    id: UUID


class CreateProdutorUsecase:
    def __init__(self, repo: ProdutorRepository) -> None:
        self._repo = repo
    
    def execute(self, input: ProdutorDTO) -> Output:
        propriedades = []
        for prop in input.propriedades:
            culturas = [
                Cultura(nome=c.nome_cultura, safra=Safra(c.safra.nome))
                for c in prop.culturas
            ]
            propriedade = PropriedadeRural(
                nome_fazenda=prop.nome_fazenda,
                area_total=prop.area_total,
                area_agricultavel=prop.area_agricultavel,
                area_vegetacao=prop.area_vegetacao,
                cidade=prop.cidade,
                estado=prop.estado,
                culturas=culturas
            )
            propriedades.append(propriedade)

        produtor = Produtor(
            documento=DocumentoIdentificacao(input.doc_identificacao),
            nome=input.nome_produtor,
            email=Email(input.email),
            telefone=Telefone(input.telefone),
            propriedades=propriedades
        )
        self._repo.save(produtor)
        return Output(id=produtor.id)