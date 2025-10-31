print(f'{'Listando números':^40}')
print('-'*40)

list_n = []
print('Insira 5 números: ')

for c in range(0,5):
    n = int(input(f'{c+1}°' ))
    if c == 0:
        list_n.append(n)
        print('Inserido no ínicio da lista...')

    elif n > list_n[-1]:
        list_n.append(n)
        print('Inserido no final da lista...')

    else:
        pos = 0
        while pos < len(list_n):
            if n<= list_n[pos]:
                list_n.insert(pos, n)
                print(f'Inserido na posição {pos+1}')
                break
            pos+=1

            

print('-'*40)
print('A lista em ordem crescente é: ',end='')
for numero in list_n:
    print(numero, end=' ')
