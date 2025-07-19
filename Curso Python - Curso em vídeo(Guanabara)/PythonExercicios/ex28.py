from random import randint

num_ale = randint(1, 5)

num = int(input('Estou pensando em um número de 1 a 5, qual você acha que é? '))

if num_ale == num:
    print(f'O número é {num_ale} parabéns você acertou! ')
else:
    print(f'O que pena você errou o número que pensei é {num_ale} ')
