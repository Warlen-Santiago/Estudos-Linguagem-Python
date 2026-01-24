def valida(v,opçoes=()):
    '''
    Verifica entre as opções fornecidas se a netrada de dados foi valida, caso não seja informa que o valor é invalido e retorna para entrada de dados
    
    :param v: Recebe o texto que aparecera para a pessoa 
    :param opçoes: Recebe as opções para verificar a validação
    '''

    escolha = input(v)[0].upper().strip()
    if escolha.isnumeric():
        escolha = int(escolha)

    while escolha not in opçoes:
        print('-'*100)
        print('\033[31mValor inserido invalido, tente novamente...\033[m ')
        print('-'*100)

        escolha = input(v)[0].upper().strip()
        if escolha.isnumeric():
            escolha = int(escolha)
    
    return escolha


def validastr(txt):
    '''
    Valida uma entrada de dados de str que contem apenas letras
    
    :param txt: recebe o texto que o usuario vera na tela
    '''
    while True:
        entrada = input(txt)
        entrada_sem_espc = entrada.split()
        resultado = ''.join(entrada_sem_espc)
        if resultado.isalpha():
            return entrada
        else:
            print('\033[;31mDado inserido invalido, tente novamente...\033[;m ')


def validaint(n):
    '''
    Verifica se a entrada de dados é um número int
    
    :param n: recebe o texto que aparecera para o usuario na tela
    '''
    
    num = input(n)
    while num.isnumeric() == False: 
        print('\033[;31mErro... O valor inserido é inavlido, tente novamente.\033[m ')
        num = input(n)

    return num

