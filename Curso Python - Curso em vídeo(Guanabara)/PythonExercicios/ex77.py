lista = ('mesa', 'azul', 'correr', 'montanha', 'doce', 'silêncio', 'avião', 'porta', 'vento', 'livro')

vogais = ('a', 'e', 'i', 'o', 'u')

for c in range(0,len(lista)):
    print()
    print(f'\033[mNa palavra \033[32m{lista[c].upper()}\033[m as vogais são:', end=' ')
    for letra in lista[c]:
        if letra in vogais:
            print(f'\033[32m{letra}', end=', ')

print('\033[m')
print()
