from rich import print
from rich.panel import Panel


canal = ['1','2','3','4','5']

c = 3
canal[c-1] = f'[green on yellow] {c} [/]'
canal1 = ' '.join(canal)


volume = ['[white on green]   ','   ','   ','   ','   [/]']

v = 6
if v == 1:
            volume[0] = '[white on green]   [/]'
            volume[1] = '[white on white]   '
            volume[4] = '   [/]'

            volume1 = ''.join(volume)

elif v == 5:
            volume1 = ''.join(volume)

elif v == 0:
            volume[0] = '[white on white]   '
            volume[4] = '   [/]'
            volume1 = ''.join(volume)

elif v in (2,3,4):
            volume[v-1] = f'   [/][white on white]'
            volume1 = ''.join(volume)

exibição = Panel(f'CANAL : {canal1}\nVOL : {volume1}', title='TV', expand=False)

print(exibição)
for c in range(0,24):
        print('')