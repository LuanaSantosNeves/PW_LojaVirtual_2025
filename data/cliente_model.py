from dataclasses import dataclass

@dataclass
class Produto:
    id: int
    nome: str
    cpf: str
    email: str
    telefone: str
    senha: str