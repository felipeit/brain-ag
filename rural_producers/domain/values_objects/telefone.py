class Telefone:
    def __init__(self, numero: str) -> None:
        if not numero.isdigit() or len(numero) < 10:
            raise ValueError("Telefone inválido.")
        self.numero = numero

    def __str__(self) -> str:
        return self.numero