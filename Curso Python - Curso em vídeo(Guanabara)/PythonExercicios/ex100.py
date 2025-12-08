from random import randint

def sorteio():
    numeros = []
    for c in range(0,5):
        numeros.append(randint(0,10))

    return numeros

def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma+=c

    return soma

n = sorteio()

print('-'*50)
print('Usando a função criada [sorteio()] para sortear 5 numeros aleatorios: ')
print()
print(f'{n}')
print('-'*50)
print(f'Usando a função criada [somapar()] conseguimos a soma entre os números pares da lista {n}, que é: ',end='')

totalpar = somapar(n)

print(totalpar)
print()
print('-'*50)
