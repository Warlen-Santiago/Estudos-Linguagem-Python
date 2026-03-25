class Pessoa: # GENERALIZADA - Classe mãe

    def __init__(self, nome='desconhecido', idade=0):
        self.nome = nome
        self. idade = idade

    def aniversario(self):
        self.idade += 1