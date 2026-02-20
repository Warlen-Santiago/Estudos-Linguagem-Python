from time import sleep
i = int(input('Escolha um inicio: '))
f = int(input('Escolha um fim: '))
pc = int(input('Escolha um parametro de contagem (ex: de 2 em 2): '))
for c in range(i, f+1, pc):
    print(c)
    sleep(0.5)