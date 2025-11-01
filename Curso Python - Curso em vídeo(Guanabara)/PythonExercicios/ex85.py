print(f'{'Analisando números':.^50}')

numeros = [[],[]]

print('Insira 7 números:')
for c in range(0,7):
    n = int(input(f'{c+1}°: '))

    if n % 2 == 0:
        #números pares
        numeros[0].append(n)
    else:
        #números ímpares
        numeros[1].append(n)

numeros[0].sort() 
numeros[1].sort()

print('.'*50)

print('Os números pares listados são: ',end='')
for n in numeros[0]:
    print(n,end=' ')

print('\nOs números ímpares listados são: ',end='')
for n in numeros[1]:
    print(n,end=' ')
print()
