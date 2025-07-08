from typing import Optional
from uuid import UUID, uuid4


class Safra:
    def __init__(self, ano: int, descricao: Optional[str] = None) -> None:
        self._ano = ano
        self._descricao = descricao or f"Safra {ano}"
        self._id = uuid4()
        
    @property
    def id(self) -> UUID:
        return self._id
    
    @property
    def ano(self) -> int:
        return self._ano

    @property
    def descricao(self) -> str:
        return self._descricao

    @ano.setter
    def ano(self, value: int) -> None:
        self._ano = value

    @descricao.setter
    def descricao(self, value: str) -> None:
        self._descricao = value or f"Safra {self._ano}"

    def __repr__(self) -> str:
        return f"<Safra {self.ano} - {self.descricao}>"
