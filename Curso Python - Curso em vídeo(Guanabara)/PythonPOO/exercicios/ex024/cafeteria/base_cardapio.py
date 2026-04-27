from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class BebidaQuente(ABC):
    def __init__(self):
        super().__init__()


    def preparar(self):
        exibir = Panel(f'1. {self.ferver_agua()}\n2. {self.misturar()}\n3. {self.servir()}', expand=False, title='Preparando...', subtitle='Bebida Pronta!')
        print(exibir)


    def ferver_agua(self):
        return f'Fervendo água a 100° graus celsius...'
    

    @abstractmethod
    def misturar(self):
        pass


    @abstractmethod
    def servir(self):
        pass
       