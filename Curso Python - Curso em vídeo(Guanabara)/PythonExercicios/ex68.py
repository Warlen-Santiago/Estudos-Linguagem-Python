from random import randint
from time import sleep

print('-'*40)
print('PAR OU IMPAR')

cont_vitorias = 0

while True:
    print('-'*40)
    print('Vamos jogar...')
    sleep(0.5)
    escolha = input('Você quer PAR ou IMPAR?[P/I]: ')[0].strip().upper()

    print('PAR...')
    sleep(0.5)
    print('OU...')
    sleep(0.5)
    print('IMPAR...')

    n_jogador = int(input('Jogue seu número de 1 a 10: '))
    n_maquina = randint(1, 10)

    print('-'*40)

    print(f'Você escolheu {n_jogador} e a maquina escolheu {n_maquina} ')

    if escolha == 'P':
        if (n_jogador + n_maquina) % 2 == 0:
            print('VOCÊ GANHOU! ')
            cont_vitorias +=1 
        else:
            print('Você perdeu...')
            break

    elif escolha == 'I':
        if (n_jogador + n_maquina) % 2 == 0:
            
            print('Você perdeu...')
            break
        else:
            print('VOCÊ GANHOU! ') 
            cont_vitorias +=1 

sleep(1)
print(f'Mas, você venceu {cont_vitorias} vezes... ')
sleep(1)
print('GAME OVER.')

