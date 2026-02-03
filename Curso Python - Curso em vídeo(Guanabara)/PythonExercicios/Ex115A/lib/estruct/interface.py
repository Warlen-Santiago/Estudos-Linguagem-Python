def linha(tam=50):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def validaint(n):
    '''
    Verifica se a entrada de dados é um número int
    
    :param n: recebe o texto que aparecera para o usuario na tela
    '''
    
    num = input(n)
    while num.isnumeric() == False: 
        print('\033[;31mError... Escolha uma opção valida e tente novamente.\033[m ')
        num = input(n)
    num = int(num)
    return num


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for i, d in enumerate(lista):
        print(f'\033[33m{i+1:>4}\033[m - \033[34m{d}\033[m')
    print(linha())
    escolha = validaint('\033[32mOpção escolhida:\033[m ')
    return escolha


