from abc import ABC, abstractmethod


class Pessoa(ABC): # GENERALIZADA - Classe mãe

    def __init__(self, nome='desconhecido', idade=0):
        self.nome = nome
        self. idade = idade


    @abstractmethod
    def estudar(self):
        pass
    

    def aniversario(self):
        self.idade += 1