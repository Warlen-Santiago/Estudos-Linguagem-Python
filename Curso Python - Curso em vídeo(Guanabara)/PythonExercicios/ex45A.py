from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura' )
computador = randint(0, 2)

print('-----------JO - KEM - PÔ-----------')

print('''Suas opções:
0 - Pedra ✊
1 - Papel ✋
2 - Tesoura ✌''')

jogador = int(input('Sua jogada é:'))
print('-=' * 20)
print('JO✊')
sleep(1)
print('KEM✊')
sleep(1)
print('PÔ✊')
sleep(1)
print('-=' * 20)

if computador == 0:
    if jogador == 0:
        print('EMPATE!✊ ✊')
    elif jogador == 1:
        print('JOGADOR GANHOU!✊ ✋')
    elif  jogador == 2:
        print('JOGADOR PERDEU!✊ ✌')
    else:
        print('Escolha uma opção valida!')
elif computador == 1:
    if jogador == 0:
        print('JOGADOR PERDEU!✋ ✊')
    elif jogador == 1:
         print('EMPATE!✋ ✋')
    elif  jogador == 2:
        print('JOGADOR GANHOU!✋ ✌')
    else:
        print('Escolha uma opção valida!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU!✌ ✊')
    elif jogador == 1:
        print('JOGADOR PERDEU!✌ ✋')
    elif  jogador == 2:
        print('EMPATE!✌ ✌')
    else:
        print('Escolha uma opção valida!')
print('-='*20)

print(f'O computador escolheu {itens[computador]} ')
print(f'E você escolheu {itens[jogador]} ')