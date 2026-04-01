from .produto import Produto
from rich import print
from rich.panel import Panel


class Alimento(Produto):
    def __init__(self, nome, marca, tipo, lote, validade, entrada, valor=0, quant=0):
        super().__init__(nome, marca, tipo, valor, quant)
        