numeros =[]

while True:
    n = int(input('Insira um número inteiro: '))

    if n in numeros:
        print('Esse número já foi listado, por favor tente novamente. ')
    else:
        numeros.append(n)
        escolha = input('Você deseja continuar?[S/N] ')[0].upper().strip()
        if escolha == 'N':
            break
    print()

numeros.sort()

print('-'*30)

print(f'Os números listados foram: ', end=' ')
for numero in numeros:
    print(numero, end=' ')