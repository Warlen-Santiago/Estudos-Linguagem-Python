from .personagem import Personagem
from rich import print, inspect
from rich.panel import Panel
from random import randint


class Guerreiro(Personagem):

    def __init__(self, nome, especie, golpes=...):
        super().__init__(nome, especie, golpes)

        self.defesa = 0.25
        self.forca = 0.30
        self.mana = 0.07

    def curar(self):
        if self.status == 'vivo':

            nlv_cura = randint(1,6)
            self.vida = self.vida + (10 * nlv_cura)

            if self.vida > 100:
                self.vida = 100

            exibir = Panel(f'[purple]{self.nome.capitalize()}-{self.__class__.__name__}[/] usou uma bandagem e curou [green]{10 * nlv_cura}[/] - vida atual: [green]{self.vida}[/]', expand=False)

            print(exibir)

        else:

            exibir = Panel(f'[purple]{self.nome.capitalize()}-{self.__class__.__name__}[/] está [red]Morto[/] - ação não executada', expand=False)

            print(exibir)

class Mago(Personagem):

    def __init__(self, nome, especie, golpes=...):
        super().__init__(nome, especie, golpes)

        self.defesa = 0.05
        self.forca = 0.10
        self.mana = 0.50      

    def curar(self):
        if self.status == 'vivo':

            nlv_cura = randint(1,6)
            self.vida = self.vida + (10 * nlv_cura)

            if self.vida > 100:
                self.vida = 100

            exibir = Panel(f'[purple]{self.nome.capitalize()}-{self.__class__.__name__}[/] usou uma poção de cura e curou [green]{10 * nlv_cura}[/] - vida atual: [green]{self.vida}[/]', expand=False)

            print(exibir)

        else:

            exibir = Panel(f'[purple]{self.nome.capitalize()}-{self.__class__.__name__}[/] está [red]Morto[/] - ação não executada', expand=False)

            print(exibir)  

class Paladino(Personagem):

    def __init__(self, nome, especie, golpes=...):
        super().__init__(nome, especie, golpes)

        self.defesa = 0.50
        self.forca = 0.20
        self.mana = 0.15  

    def curar(self):
        if self.status == 'vivo':

            nlv_cura = randint(1,6)
            self.vida = self.vida + (10 * nlv_cura)

            if self.vida > 100:
                self.vida = 100

            exibir = Panel(f'[purple]{self.nome.capitalize()}-{self.__class__.__name__}[/] recebeu benção e curou [green]{10 * nlv_cura}[/] - vida atual: [green]{self.vida}[/]', expand=False)

            print(exibir)

        else:

            exibir = Panel(f'[purple]{self.nome.capitalize()}-{self.__class__.__name__}[/] está [red]Morto[/] - ação não executada', expand=False)

            print(exibir) 
                                                  #------------TESTES------------#
