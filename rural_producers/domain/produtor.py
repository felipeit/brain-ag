from typing import List, Optional
from uuid import UUID, uuid4

from rural_producers.domain.propriedade_rural import PropriedadeRural
from rural_producers.domain.values_objects.documento_identificacao import DocumentoIdentificacao
from rural_producers.domain.values_objects.email import Email
from rural_producers.domain.values_objects.telefone import Telefone


class Produtor:
    def __init__(
        self, 
        documento: DocumentoIdentificacao,
        nome: str,
        email: Email,
        telefone: Telefone,
        propriedades: Optional[List[PropriedadeRural]] = None
    ) -> None:
        if not documento:
            raise ValueError("CPF/CNPJ é obrigatório")
        if not nome:
            raise ValueError("Nome do produtor é obrigatório")
        self._id = uuid4()
        self._documento = documento
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._propriedades = propriedades or []
        self._errors = []
    
    @property
    def id(self) -> UUID:
        return self._id
    
    @property
    def documento(self) -> DocumentoIdentificacao:
        return self._documento

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def email(self) -> Email:
        return self._email

    @property
    def telefone(self) -> Telefone:
        return self._telefone

    @property
    def propriedades(self) -> List[PropriedadeRural]:
        return self._propriedades

    @id.setter
    def id(self, value) -> None:
        self._id = value
    
    @documento.setter
    def documento(self, value: DocumentoIdentificacao) -> None:
        if not value:
            raise ValueError("Documento inválido")
        self._documento = value
    
    @nome.setter
    def nome(self, value: str) -> None:
        if not value:
            raise ValueError("Nome é obrigatório")
        self._nome = value

    @email.setter
    def email(self, value: Email) -> None:
        self._email = value

    @telefone.setter
    def telefone(self, value: Telefone) -> None:
        self._telefone = value

    @propriedades.setter
    def propriedades(self, value: List[PropriedadeRural]) -> None:
        self._propriedades = value or []

    def adicionar_propriedade(self, propriedade: PropriedadeRural) -> None:
        if propriedade not in self._propriedades:
            self._propriedades.append(propriedade)

    def __repr__(self) -> str:
        return f"<Produtor {self.nome} - CPF/CNPJ: {self.documento}>"
