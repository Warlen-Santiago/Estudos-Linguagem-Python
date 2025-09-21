n = int(input('Insira um número inteiro qualquer e veja seu fatorial: '))
n2 = n-1

while n2 != 0:
    n = n*n2
    n2 = n2-1

print(f'O resultado é: {n} ')
