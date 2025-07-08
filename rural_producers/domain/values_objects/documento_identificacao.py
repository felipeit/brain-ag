from validate_docbr import CPF, CNPJ

class DocumentoIdentificacao:
    def __init__(self, valor: str) -> None:    
        valor = valor.strip().replace(".", "").replace("-", "").replace("/", "")
        if not valor:
            raise ValueError("Documento de identificação não pode ser vazio.")
        if len(valor) == 11:
            if not CPF().validate(valor):
                raise ValueError("CPF inválido.")
        elif len(valor) == 14:
            if not CNPJ().validate(valor):
                raise ValueError("CNPJ inválido.")
        else:
            raise ValueError("Documento deve conter 11 (CPF) ou 14 (CNPJ) dígitos.")

        self.valor = valor

    def __eq__(self, other) -> bool:
        return isinstance(other, DocumentoIdentificacao) and self.valor == other.valor

    def __str__(self) -> str:
        return self.valor