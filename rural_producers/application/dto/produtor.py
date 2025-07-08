from typing import List
from uuid import UUID
from pydantic import BaseModel
from rural_producers.application.dto.propriedade import PropriedadeDTO


class ProdutorDTO(BaseModel):
    doc_identificacao: str
    nome_produtor: str
    email: str
    telefone: str
    propriedades: List[PropriedadeDTO]
    id: UUID = None