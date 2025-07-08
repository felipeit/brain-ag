from uuid import UUID, uuid4
from rural_producers.domain.safra import Safra


class Cultura:
    def __init__(self, nome: str, safra: Safra) -> None:
        self._nome = nome
        self._safra = safra
        self._id = uuid4()
        if not self._nome:
            raise ValueError("Nome da cultura não pode ser vazio")
    
    @property
    def id(self) -> UUID:
        return self._id
    
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def safra(self) -> Safra:
        return self._safra

    @nome.setter
    def nome(self, value: str) -> None:
        if not value:
            raise ValueError("Nome da cultura não pode ser vazio")
        self._nome = value

    @safra.setter
    def safra(self, value: Safra) -> None:
        self._safra = value

    def __repr__(self) -> str:
        return f"<Cultura {self.nome}>"
