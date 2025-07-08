from typing import List

from pydantic import BaseModel
from rural_producers.application.dto.cultura import CulturaDTO


class PropriedadeDTO(BaseModel):
    nome_fazenda: str
    area_agricultavel: float
    area_vegetacao: float
    area_total: float
    cidade: str
    estado: str
    culturas: List[CulturaDTO]