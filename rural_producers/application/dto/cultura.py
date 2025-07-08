from pydantic import BaseModel
from rural_producers.application.dto.safra import SafraDTO


class CulturaDTO(BaseModel):
    nome_cultura: str
    safra: SafraDTO