def valida(v,opçoes=()):

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