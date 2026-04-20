from rich import print
from rich.panel import Panel


class Produto():
    def __init__(self, nome, marca, tipo, valor=0.00, quant=0):
        self.nome = nome
        self.marca = marca
        self.tipo = tipo
        self.valor = valor
        self.quant = quant
    
    def vender(self, quant_venda=1):
        self.quant -= quant_venda

        exibir = Panel(f'Foram vendidos (a) [green]{quant_venda} unidade (s) de {self.nome}, {self.marca}[/], estoque atual é de [green]{self.quant}[/] ', expand=False)

        return exibir
        
    def repor(self, quant_repor):
        self.quant += quant_repor

        exibir = Panel(f'Foram repostos [green]{quant_repor} de {self.nome}, {self.marca}[/], estoque atual de [green]{self.quant}[/] ', expand=False)

        return exibir
