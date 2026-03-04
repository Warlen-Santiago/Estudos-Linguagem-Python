from rich import print
from rich.panel import Panel


class Produto():
    def __init__(self, nome='Não informado', preço=0.0):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        q = len(self.nome) 
        etq = Panel(f'{self.nome}\n{'-'*q}\n[green]R$ {self.preço:.2f}[/]', expand=False)
        return etq
    
p1 = Produto('Garrafa de Água', 32.50)
p2 = Produto('PC Gamer', 3600)

print(p1.etiqueta())
print(p2.etiqueta())
