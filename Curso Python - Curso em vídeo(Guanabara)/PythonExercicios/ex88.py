from random import randint
from time import sleep

print(f'{'PALPITES DA MEGA':^50} ')
print('-'*50)

qunt = int(input('Quantos palpites você deseja: '))

print('Gerando palpites: ',end='')
for o in range(0,3):
    print('.',end='')
    sleep(1)
print()

palpites = []
total_palpites =[]

for c in range(0,qunt):
    while len(palpites) != 6:
        p = randint(0,60)

        if p not in palpites:
            palpites.append(p)

    total_palpites.append(palpites[:])
    palpites.clear()

print('\nOs palpites gerados foram: ')
print()
sleep(1)

for cont, palp in enumerate(total_palpites):
    print(f'''{cont+1}°: {palp}''')
    sleep(0.5)

print('-'*50)