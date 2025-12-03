def maior(n):
    m = 0
    for i, c in enumerate(n):
        if i == 0:
            m = c
        elif c > m:
            m = c
            
    print(f'E o maior número da lista é: {m}')

def linha():
    print('-'*50)


linha()
print(f'{'LISTA DE NÚMEROS':^50}')
linha()


numeros = []
cont=1
while True:
    numero = int(input(f'Insira o {cont}° número: '))
    numeros.append(numero)
    cont+=1

    escolha =''
    while escolha not in ('N','S'):
        escolha = input('Deseja continuar?[S/N] ')[0].upper().strip()
    linha()
    if escolha == 'N':
        break
    

print('Sua lista de números ficou assim: ')
for c in numeros:
    print(c,end='-')
print('FIM.')
print()

maior(numeros)
print()
