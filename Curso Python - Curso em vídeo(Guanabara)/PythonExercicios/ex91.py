from random import randint
from time import sleep
from operator import itemgetter

print(f'{'JOGANDO DADOS':^50}')
print('-'*50)
jogadores = {
    'jogador.1': randint(1,6),
    'jogador.2': randint(1,6),
    'jogador.3': randint(1,6),
    'jogador.4': randint(1,6)
}

for k, v in jogadores.items():
    print(f'O {k} jogou: {v} ')
    sleep(1)

rank = []
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-'*50)
sleep(1)
print(f'O maior resultado foi: {max(jogadores['jogador.1'],jogadores['jogador.2'],jogadores['jogador.3'],jogadores['jogador.4'])}')
sleep(1)
print('-'*50)
sleep(1)
print(f'O menor resultado foi: {min(jogadores['jogador.1'],jogadores['jogador.2'],jogadores['jogador.3'],jogadores['jogador.4'])}')
sleep(1)
print('-'*50)
sleep(1)
print('O placar foi: ')
sleep(1)

for num, v in enumerate(rank):
    print(f'{num+1}° lugar - {v[0]} tirou: {v[1]} ')
    sleep(1)
print('-'*50)
print()
    