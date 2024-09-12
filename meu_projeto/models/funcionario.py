from models.enum.sexo import Sexo
from models.enum.setor import Setor

class Funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"Id: {self.id}"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSalario: {self.salario}"
            f"\nSetor: {self.setor}"
            f"\nSexo: {self.sexo}"
        )    