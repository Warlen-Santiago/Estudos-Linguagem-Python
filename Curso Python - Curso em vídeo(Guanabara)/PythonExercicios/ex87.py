print(f'{'MATRIZ':^30}')
print('-'*30)

matriz = [[],[],[]]
somap = 0
soma3c = 0
maior2l = 0
for c in range(0,3):
    for inx in range(0,3):
        n = int(input(f'Adicione um número para a posição [{c}][{inx}]: '))
        matriz[c].append(n)

        if n % 2 == 0:
            somap+=n
        if inx == 2:
            soma3c+=n

        if c == 1 and inx == 0:
            maior2l = n
        elif c == 1 and n>maior2l:
            maior2l = n

print('-'*30)

print('Sua matriz ficou assim: ')
print()

for c in matriz:
    print(f'''           {c}''')
print()
print('-'*30)

print(f'A soma de todos os valores pares é: {somap} ')
print()
print(f'A soma dos valores da terceira coluna é: {soma3c} ')
print()
print(f'O maior número da segunda linha é: {maior2l} ')
print()
