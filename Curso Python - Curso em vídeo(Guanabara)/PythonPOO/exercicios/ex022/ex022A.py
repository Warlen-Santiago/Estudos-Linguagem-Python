from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min = 1
    canal_max = 6
    volume_min = 1
    volume_max = 5

    def __init__(self, canal=1,volume=1):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def mostrar_tv(self):

        if not self.ligado:
            conteudo = f'[red]A TV está desligada[/]'

        else:
            conteudo = f'CANAL:\nVOLUME:'

        tv = Panel(conteudo, title='[ TV ]', expand=False)
        print(tv)
    
tv1 = ControleRemoto()
tv1.liga_desliga()
tv1.mostrar_tv()