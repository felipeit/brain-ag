from pydantic import BaseModel


class SafraDTO(BaseModel):
    nome: str