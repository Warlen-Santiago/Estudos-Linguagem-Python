from rich import print
from rich.panel import Panel
from time import sleep


class ControleRemoto():
    def __init__(self):
        self.situação = 'desligada'
        self.canal = 1
        self.volume = 1

    def liga_desliga(self):
        if self.situação == 'desligada':
            self.situação = 'ligada'
        else:
            self.situação = 'desligada'

    def vol(self, v):
        if self.situação == 'ligada':
            if v == '+':
                if self.volume == 5:
                    self.volume = 5
                else:
                    self.volume +=1

            elif v == '-':
                if self.volume == 0:
                    self.volume = 0
                else:
                    self.volume -=1
        
    def can(self,c):
        if self.situação == 'ligada':
            if c == '>':
                if self.canal == 5:
                    self.canal = 1
                else:
                    self.canal += 1
            elif c == '<':
                if self.canal == 1:
                    self.canal = 5
                else:
                    self.canal -= 1

    def exibir(self):
        
        if self.situação == 'ligada':
            #DEFININDO CANAL
            canal = ['1','2','3','4','5']

            canal[self.canal-1] = f'[green on yellow] {self.canal} [/]'
            canal1 = ' '.join(canal)

            #DEFININDO VOLUME
            volume = ['[white on green]   ','   ','   ','   ','   [/]']
        
            
            if self.volume == 1:
                volume[0] = '[white on green]   [/]'
                volume[1] = '[white on white]   '
                volume[4] = '   [/]'

                volume1 = ''.join(volume)

            elif self.volume == 5:
                volume1 = ''.join(volume)

            elif self.volume == 0:
                volume[0] = '[white on white]   '
                volume[4] = '   [/]'
                volume1 = ''.join(volume)

            elif self.volume in (2,3,4):
                volume[self.volume-1] = f'   [/][white on white]'
                volume1 = ''.join(volume)

            exibição = Panel(f'CANAL : {canal1}\nVOL : {volume1}', title='[TV]', expand=False)

            return exibição
        else:
            exibição = Panel(f'[purple]A TV esta [/][red]desligada![/] ', title='[TV]', expand=False)

            return exibição

meu_controle = ControleRemoto()

escolha =''
while True:
    
    for c in range (0,30):
        print('')

    print(meu_controle.exibir())
    escolha = input('')

    if escolha in ('+','-'):
        meu_controle.vol(escolha)

    elif escolha in ('<','>'):
        meu_controle.can(escolha)

    elif escolha == '@':
        meu_controle.liga_desliga()

    elif escolha == '0':
        break

    elif escolha == '?':
        print('Controle remoto:\n- volume : + ou -\n- canal : < ou >\n- ligar ou desligar : @\n- "0" fecha o programa')
        sleep(7)
    else:
        print('\nBotão [red]invalido[/], a TV não responde (digite "?" para consultar o manual do controle)')
        sleep(5)
    