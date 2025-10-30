print(f'{'MATRIZ':^30}')
print('-'*30)

matriz = [[],[],[]]

for c in range(0,3):
    for inx in range(0,3):
        matriz[c].append(int(input(f'Adicione um número para a posição [{c}][{inx}]: ')))

print('-'*30)

print('Sua matriz ficou assim: ')
print()

for c in matriz:
    print(f'''           {c}''')
print()
