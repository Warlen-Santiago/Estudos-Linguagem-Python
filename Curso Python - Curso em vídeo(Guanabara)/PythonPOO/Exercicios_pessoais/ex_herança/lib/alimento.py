from .produto import Produto
from rich import print
from rich.panel import Panel
from datetime import date


class Alimento(Produto):
    def __init__(self, nome, marca, tipo, lote, validade=(0000,00,00), valor=0, quant=0):
        super().__init__(nome, marca, tipo, valor, quant)
        self.lote = lote
        self.validade = date(*validade)
         
    def vencimento(self):
        data_atual = date.today()

        if data_atual < self.validade:
            exibir = Panel(f'O produto {self.nome} da marca {self.marca} [green]vencera em {self.validade}[/] ', expand=False, title=self.lote)
            return exibir
        
        else:
            exibir = Panel(f'O produto {self.nome} da marca {self.marca} [red]venceu em {self.validade}[/] ', expand=False, title=self.lote)
            return exibir
