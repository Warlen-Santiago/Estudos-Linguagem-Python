from random import randint

print('-jokempô- ')
ej = int(input('Escolha:\n 1-pedra\n 2-papel\n 3-tesoura \n '))
em = randint(1, 3)

if ej == em:
    print('Deu empate! ')
elif ej == 1 and em == 2 or ej == 2 and em == 3 or ej == 3 and em == 1:
    print('Você perdeu!!')
elif ej == 2 and em == 1 or ej == 3 and em == 2 or ej == 1 and em ==3:
    print('Você ganhou!!')
