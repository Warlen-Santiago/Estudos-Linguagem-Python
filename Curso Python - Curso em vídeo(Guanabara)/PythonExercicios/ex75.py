lista = []
print('Insira 4 números inteiros: ')
for c in range(0,4):
    n = int(input(f'{c+1}°: '))
    lista.append(n)

tupla = tuple(lista)

print(tupla)

print(f'O número 9 foi digitado {tupla.count(9)} veze(s)')

if 3 not in tupla:
    print('O número 3 não está entre os números digitados. ')
else:
    print(f'O número 3 foi digitado pela primeira vez na posição {tupla.index(3)+1}')
print('Os número(s) pares digitados foram: ')
for c in tupla:
    if c % 2 == 0:  
        print(f'{c},', end=' ')