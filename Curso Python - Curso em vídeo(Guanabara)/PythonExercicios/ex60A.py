n = int(input('Insira um número inteiro qualquer e veja seu fatorial: '))
total = n

for c in range(1, n,):
    total = total * c


print(f'O fatorial de {n} é {total}')