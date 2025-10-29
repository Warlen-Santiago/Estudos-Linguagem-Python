print('Listagem de números... ')
print('-'*40)

numeros = []
while True:
    n = int(input('Insira um número: '))
    numeros.append(n)

    escolha =''
    while escolha not in ('N','S'):
        escolha = input('Deseja continuar?[S/N] ')[0].upper().strip()

    if escolha == 'N':
        break
    print()

n_impares =[]
n_pares =[]

for numero in numeros:
    if numero % 2 == 0:
        n_pares.append(numero)
    else:
        n_impares.append(numero)

print('-'*40)

print(f'Os números inseridos foram: {numeros} ')
print(f'Entre eles os números pares são: {n_pares} ')
print(f'E os ímpares: {n_impares} ')
