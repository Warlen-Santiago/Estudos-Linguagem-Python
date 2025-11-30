def contador(i,f,p):

    print(f'-De {i} a {f} de 1 em 1: ')
    print()
    for c in range(i,f+1):
        print(c,end=' ')
    print()
    linha()

    print(f'-De {f} a {i} de -2 em -2: ')
    print()

    for c in range(f, i-1, -2):
        print(c, end=' ')
    print()
    linha()

    print(f'-De {i} a {f} de {p} em {p}: ')
    print()

    for c in range(i, f+1, p):
        print(c,end=' ')
    print()
    linha()


def linha():
    print('-'*50)


linha()
print(f'{'-CONTADOR-':^50}')
linha()

inicio = int(input('Sua contagem começara de qual número: '))
fim = int(input('Finalizara em qual: '))
parametro = int(input('E tera qual parametro: '))
linha()

contador(inicio, fim, parametro)

