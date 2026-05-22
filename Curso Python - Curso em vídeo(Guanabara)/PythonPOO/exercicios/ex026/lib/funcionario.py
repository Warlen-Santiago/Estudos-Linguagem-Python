from abc import ABC, abstractmethod
from rich.panel import Panel


class Funcionario(ABC):

    SAL_MIN = 1621
    INSS = 0.075

    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_liquido = 0
        
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
         exibir = Panel(f'[yellow]{self.nome}[/] tem [red]salário bruto[/] de [red]R${self.sal_bruto:.2f}[/] e [green]salário líquido[/] de [green]R${self.sal_liquido:.2f}[/] - que equivale a [yellow]{(self.sal_bruto/Funcionario.SAL_MIN):.1f} salários minimos[/]', expand=False, title='[purple]Analise salárial[/]')

         return exibir