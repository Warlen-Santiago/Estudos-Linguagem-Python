from rich import print, inspect
from clss_espc import Aluno, Professor, Funcionario


aluno1 = Aluno(nome='Warlen', idade=21, curso='ADS', turma=66)
aluno1.matricula()

professor1 = Professor('Marcos', 32, 'Farmacia', 3)
professor1.dar_aula()

funcionario1 = Funcionario('Felipe', 27, 'Examinador', 'RH')
funcionario1.bater_ponto()
