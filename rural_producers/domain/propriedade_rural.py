from typing import List, Optional
from uuid import uuid4, UUID
from rural_producers.domain.cultura import Cultura


class PropriedadeRural:
    def __init__(
        self,
        nome_fazenda: str, 
        cidade: str, 
        estado: str, 
        area_total: float, 
        area_agricultavel: float, 
        area_vegetacao: float,
        culturas: Optional[List[Cultura]] = None
    ) -> None:
        self._id = uuid4()
        self._nome_fazenda = nome_fazenda
        self._cidade = cidade
        self._estado = estado
        self._area_total = area_total
        self._area_agricultavel = area_agricultavel
        self._area_vegetacao = area_vegetacao
        self._culturas = culturas or []

        self._validar_areas()

    def _validar_areas(self) -> None:
        if self._area_total < self._area_agricultavel + self._area_vegetacao:
            raise ValueError("Área total não comporta a soma de agricultável e vegetação.")

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def nome_fazenda(self) -> str:
        return self._nome_fazenda

    @property
    def cidade(self) -> str:
        return self._cidade

    @property
    def estado(self) -> str:
        return self._estado

    @property
    def area_total(self) -> float:
        return self._area_total

    @property
    def area_agricultavel(self) -> float:
        return self._area_agricultavel

    @property
    def area_vegetacao(self) -> float:
        return self._area_vegetacao

    @property
    def culturas(self) -> List[Cultura]:
        return self._culturas


    @nome_fazenda.setter
    def nome_fazenda(self, value: str) -> None:
        self._nome_fazenda = value

    @cidade.setter
    def cidade(self, value: str) -> None:
        self._cidade = value

    @estado.setter
    def estado(self, value: str) -> None:
        self._estado = value

    @area_total.setter
    def area_total(self, value: float) -> None:
        self._area_total = value
        self._validar_areas()

    @area_agricultavel.setter
    def area_agricultavel(self, value: float) -> None:
        self._area_agricultavel = value
        self._validar_areas()

    @area_vegetacao.setter
    def area_vegetacao(self, value: float) -> None:
        self._area_vegetacao = value
        self._validar_areas()

    @culturas.setter
    def culturas(self, value: List[Cultura]) -> None:
        self._culturas = value or []

    def adicionar_cultura(self, cultura: Cultura) -> None:
        if cultura not in self._culturas:
            self._culturas.append(cultura)

    def __repr__(self) -> str:
        return (
            f"<PropriedadeRural {self.nome_fazenda} - {self.cidade}/{self.estado}, "
            f"Área total: {self.area_total}ha>"
        )
