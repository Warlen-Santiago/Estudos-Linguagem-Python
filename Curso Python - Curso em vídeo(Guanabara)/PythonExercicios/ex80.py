print(f'{'Listando números':^40}')
print('-'*40)

list_n = []
print('Insira 5 números: ')
for c in range(0,5):
    n = int(input(f'{c+1}°' ))
    list_n.append(n)
    list_n.sort()
    if list_n.index(n) == 0:
        print('Adicionado no início da lista... ')
    elif list_n.index(n)+1 == len(list_n):
        print('Adicionado no final da lista... ')
    else:
        print(f'Adicionado na posição {list_n.index(n)+1}... ')

print('-'*40)
print('A lista em ordem crescente é: ',end='')
for numero in list_n:
    print(numero, end=' ')
