from abc import ABC, abstractmethod
from rich import print, inspect
from rich.panel import Panel
from random import randint



class Personagem(ABC):

    VIDA_MIN = 100

    def __init__(self, nome, especie, golpes = [{'nome_atk': 'ataque basico' , 'dano_atk': 10}]):
        self.nome = nome
        self.especie = especie
        self.golpes = golpes 
        self.status = 'vivo'
        self.vida = Personagem.VIDA_MIN
        self.defesa = 0

    @abstractmethod
    def curar(self):
        pass

    def atacar(self,alvo):
        if self.status == 'vivo':

            copia_atk = self.golpes[:]
            n = len(copia_atk)
            golpe_escolhido = randint(0,n-1)

            dano_final = self.golpes[golpe_escolhido]['dano_atk'] + (self.golpes[golpe_escolhido]['dano_atk'] * (self.mana + self.forca))

            exibir = Panel(f'[blue]{self.nome.capitalize()}-{self.__class__.__name__}[/] atacou [purple]{alvo.nome.capitalize()}-{alvo.__class__.__name__}[/] com - {self.golpes[golpe_escolhido]['nome_atk'].upper()} - ', expand=False)
            
            print(exibir)
            alvo.receber_dano(dano_final)

        else:

            exibir = Panel(f'[purple]{self.nome.capitalize()}-{self.__class__.__name__}[/] está [red]Morto[/] - ação não executada', expand=False)

            print(exibir)

    def receber_dano(self, dano):

        self.vida =  self.vida - (dano - (dano * self.defesa))

        if self.vida <= 0:
            self.status = 'morto'
        
        exibir = Panel(f'[purple]{self.nome.capitalize()}-{self.__class__.__name__}[/] recebeu [red]{dano - (dano * self.defesa):.0f}[/] de dano - {'personagem [red]Derrotado[/]' if self.status == 'morto' else f'vida atual: [green]{self.vida}[/]' } ', expand=False)

        print(exibir)
        

                                                  #------------TESTES------------#
