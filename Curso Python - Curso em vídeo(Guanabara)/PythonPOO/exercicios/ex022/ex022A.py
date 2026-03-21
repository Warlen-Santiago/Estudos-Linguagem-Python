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

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual+=1


    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual-=1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual+=1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual-=1

    def mostrar_tv(self):

        if not self.ligado:
            conteudo = f'[red]📺 🚫 A TV está desligada[/]'

        else:

            conteudo = 'CANAL: '

            for c in range (ControleRemoto.canal_min,ControleRemoto.canal_max+1):

                if c == self.canal_atual:
                    conteudo += f'[yellow on yellow] {c} [/]'

                else:
                    conteudo += f' {c} '

            conteudo += '\nVOLUME: '

            for v in range(ControleRemoto.volume_min,ControleRemoto.volume_max+1):

                if v <= self.volume_atual:
                    conteudo += f'[green on green]   [/]'

                else:
                    conteudo += f'[green on white]   [/]'

        tv = Panel(conteudo, title='[ TV ]', expand=False)
        print(tv)
    
tv1 = ControleRemoto()

while True:

    print('\n'*30)
    tv1.mostrar_tv()

    comando = input(' < CH >  - VOL + \n')

    match comando:
        case '0':
            break
        case '@':
            tv1.liga_desliga()
        case '<':
            tv1.canal_menos()
        case '>':
            tv1.canal_mais()
        case '+':
            tv1.volume_mais()
        case '-':
            tv1.volume_menos()
