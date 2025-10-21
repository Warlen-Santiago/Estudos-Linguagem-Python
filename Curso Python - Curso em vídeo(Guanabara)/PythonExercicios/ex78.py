print('Insiira 5 valores: ')

numeros =[]

print('-'*30)

for c in range(0,5):
    n = float(input(f'{c+1}°: '))

    numeros.append(n)

print('-'*30)

maiorn = max(numeros)
menorn = min(numeros)

pmaiorn = []
if numeros.count(maiorn) > 1:
    for p,n in enumerate(numeros):
        if n == maiorn:
            pmaiorn.append(p)

    print(f'O maior número é {maiorn} e o próprio aparece nas posições: ', end='')
    for c in pmaiorn:
        print(c+1, end=' ')
    print('\n')
else:
    print(f'O maior número é {maiorn} e o próprio aparece na posição: {numeros.index(maiorn)+1} ')

pmenorn = []
if numeros.count(menorn) > 1:
    for p,n in enumerate(numeros):
        if n == menorn:
            pmenorn.append(p)

    print(f'O menor número é {menorn} e o próprio aparece nas posições: ', end='')
    for c in pmenorn:
        print(c+1, end=' ')
else:
    print(f'O menor número é {menorn} e o próprio aparece na posição: {numeros.index(menorn)+1} ')
print()
