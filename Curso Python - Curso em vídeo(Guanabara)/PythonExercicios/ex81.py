print('LENDO NÚMEROS... ')
print('-'*30)
numeros = []
while True:
    n = int(input('insira um número:'))
    numeros.append(n)

    escolha=''
    while escolha not in ('N','S'):
        escolha = input('Deseja continuar?[S/N] ')[0].upper().strip()

    print()

    if escolha == 'N':
        break
print('-'*30)
print(f'Foram digitados {len(numeros)} números. ')

print('Os valores listados em ordem decrescente é: ',end='')
numeros.sort(reverse=True)
for numero in numeros:
    print(numero, end=' ')

if numeros.count(5) == 0:
    print('\nO valor 5 não foi digitado. ')
else:
    print('\nO valor 5 foi digitado. ')
    