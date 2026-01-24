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
        print('-'*30)
        print('\033[31mValor inserido invalido, tente novamente...\033[m ')
        print('-'*30)

        escolha = input(v)[0].upper().strip()
        if escolha.isnumeric():
            escolha = int(escolha)
    
    return escolha