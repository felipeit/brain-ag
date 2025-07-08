class DocumentoIdentificacao:
    def __init__(self, valor: str) -> None:
        if not valor:
            raise ValueError("Documento de identificação inválido.")
        self.valor = valor

    def __eq__(self, other) -> bool:
        return isinstance(other, DocumentoIdentificacao) and self.valor == other.valor

    def __str__(self) -> str:
        return self.valor