import os
from models.funcionario import Funcionario
from models.enum.setor import Setor
from models.enum.sexo import Sexo

os.system("cls || clear")

funcionario = Funcionario(123, "Wagner", 19, 2300, Setor.MARKETING.value, Sexo.MASCULINO.value)

print(funcionario)