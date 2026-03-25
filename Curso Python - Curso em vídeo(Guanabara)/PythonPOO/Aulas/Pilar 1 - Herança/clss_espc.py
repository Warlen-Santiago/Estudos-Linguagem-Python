from clss_gene import Pessoa


class Aluno(Pessoa): # Classes ESPECIALIZADAS - Classes filhas
    def __init__(self, nome='desconhecido', idade=0, curso='desconhecido', turma=0):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def matricula(self):
        print(f'{self.nome} fez sua matricula! ')


class Professor(Pessoa):
    def __init__(self, nome='desconhecido', idade=0, especialidade='desconhecido', nivel=1):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} iniciou uma aula! ')


class Funcionario(Pessoa):
    def __init__(self, nome='desconhecido', idade=0, cargo='desconhecido', setor='desconhecido'):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor 

    def bater_ponto(self):
        print(f'{self.nome} bateu ponto! ')
