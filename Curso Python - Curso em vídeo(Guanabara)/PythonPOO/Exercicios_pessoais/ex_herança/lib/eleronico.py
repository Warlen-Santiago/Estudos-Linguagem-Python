from .produto import Produto
from rich import print
from rich.panel import Panel


class Eletronico(Produto):
    def __init__(self, nome, marca, tipo, ano, garantia = 1, valor=0, quant=0):
        super().__init__(nome, marca, tipo, valor, quant)
        self.ano = ano
        self.garantia = garantia

    def __str__(self): #SUBISTITUIR POR UM FOR DO __DICT__ PARA ADICIONAR CORES
        exibir = Panel(f'''Produto: {self.nome}
                       Marca: {self.marca}
                       Ano: {self.ano}
                       Tempo de Garantia: {self.garantia} anos
                       Valor: R${self.valor:.2f}
                       Quantidade disponivel: {self.quant} unidades''', expand=False)
        return exibir
