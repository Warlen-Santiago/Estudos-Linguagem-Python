from abc import ABC, abstractmethod
from rich import print, inspect


class Personagem():

    VIDA_MIN = 100

    def __init__(self, nome, especie, golpes = [{'nome': 'ataque basico' , 'dano': 10}]):
        self.nome = nome
        self.especie = especie
        self.golpes = golpes 
        self.status = 'vivo'
        self.vida = Personagem.VIDA_MIN
        self.defesa = 0

    @abstractmethod
    def curar(self):
        pass

    @abstractmethod
    def atacar(self):
        pass

    def receber_dano(self, dano):

        self.vida =  self.vida - (dano - (dano * self.defesa))

        if self.vida <= 0:
            self.status = 'morto'
        
        print(f'[purple]{self.nome}[/] recebeu [red]{dano - (dano * self.defesa):.0f}[/] de dano - {'personagem [red]Derrotado[/]' if self.status == 'morto' else f'vida atual: [green]{self.vida}[/]' } ')
        

                                                  #------------TESTES------------#


'''list_golpes = [{
    'nome_atk' : 'Chute',
    'dano_atk' : 10
},{
    'nome_atk' : 'soco',
    'dano_atk' : 10
}]
p1 = Personagem('Valdir', 'Humano', list_golpes)

p1.receber_dano(10)'''
    

