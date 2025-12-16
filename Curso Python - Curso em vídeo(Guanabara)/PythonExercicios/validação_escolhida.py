def valida(v,opçoes=()):

    escolha = input(v)[0].upper().strip()
    if escolha.isnumeric():
        escolha = int(escolha)

    while escolha not in opçoes:
        print('\033[31m', end='')
        print('-'*50)
        print('Valor inserido invalido, tente novamente...')
        print('-'*50)
        print('\033[m')

        escolha = input(v)[0].upper().strip()
        if escolha.isnumeric():
            escolha = int(escolha)
    
    return escolha