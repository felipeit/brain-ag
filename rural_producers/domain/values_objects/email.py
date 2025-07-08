class Email:
    def __init__(self, endereco: str) -> None:
        if "@" not in endereco:
            raise ValueError("Email inválido.")
        self.endereco = endereco

    def __str__(self) -> str:
        return self.endereco