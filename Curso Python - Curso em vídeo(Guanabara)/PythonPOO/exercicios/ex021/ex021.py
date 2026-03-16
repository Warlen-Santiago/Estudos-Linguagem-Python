from rich import print


class Caneta():
    def __init__(self, cor='Branco'):
        self.cor = cor
        self.tampa = False

        if self.cor.lower() == 'branco':
            self.cor = 'white'

        elif self.cor.lower() == 'vermelho':
            self.cor = 'red'

        elif self.cor.lower() == 'verde':
            self.cor = 'green'

        elif self.cor.lower() == 'azul':
            self.cor = 'blue'

        elif self.cor.lower() == 'roxo':
            self.cor = 'purple'

        elif self.cor.lower() == 'laranja':
            self.cor = 'orange'

        elif self.cor.lower() == 'amarelo':
            self.cor = 'yellow'

        elif self.cor.lower() == 'preto':
            self.cor = 'black'


    def destampar(self):
        self.tampa = True

    def tampar(self):
        self.tampa = False

    def quebra_linha(self,q=1):
        for c in range(0,q):
            print('')

    def escrever(self,txt):
        if self.tampa:
            print(f'[{self.cor}]{txt}[/]')
        else:
            print('🚫[red] Sua caneta está[/][purple] tampada[/],[red] a [/][purple]destampe[/] [red] para escrever![/]🖊️✍️ ')


caneta1 = Caneta('vermelho')
caneta1.destampar()
caneta1.escrever('Mixerica')
caneta1.quebra_linha(3)
caneta1.escrever('Mixerica')
caneta1.quebra_linha()
        