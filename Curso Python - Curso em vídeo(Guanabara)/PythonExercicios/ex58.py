from random import randint

'''Gerando um número aleatorio'''
num_aleatorio = randint(1, 10)
'''iniciando o contador de tentativas'''
contador_de_tentativas = 0
'''iniciando a variavel que recebe o n do usuarío para comparação, necessario pois ele é presente no laço while, então precsa ser iniciado antes'''
num = 0

while num != num_aleatorio:
    print('-'*10, f'{contador_de_tentativas+1}° TENTATIVA', '-'*10)
    num = int(input('Um número de 1 a 10, qual você acha que é? '))
    contador_de_tentativas += 1
    if num < num_aleatorio:
        print('um pouco mais, tente novamente! ')
        print()
    elif num > num_aleatorio:
        print('Um pouco menos, tente novamente! ')
        print()

print(f'O número é {num_aleatorio} parabéns você acertou! ')
print()
print(f'Tentou {contador_de_tentativas} vezes. ')

