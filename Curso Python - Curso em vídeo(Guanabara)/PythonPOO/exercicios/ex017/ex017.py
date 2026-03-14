from rich import print
from rich.panel import Panel


class Produto():
    def __init__(self, nome='Não informado', preço=0.0):
        self.nome = nome
        self.preço = preço

    def __str__(self):
        return f'O profuto {self.nome} custa {self.preço}'

    def etiqueta(self):
        preço = f'R$ {self.preço:.2f}'
        etq = Panel(f'{self.nome.center(30, ' ')}\n{'-'*30}\n[green]{preço.center(30,' ')}[/]', expand=False)
        return etq
    
p1 = Produto('Garrafa de Água', 32.50)
p2 = Produto('PC Gamer', 3600)

print(p1.etiqueta())
print(p2.etiqueta())
