def titulo(txt):
    '''
    Cria um titulo em letras maiusculas centralizado em um sublinhado de 50 caracteres a partir da string fornecida
    
    :param txt: Recebe a string do titulo
    '''
    print('-'*100)
    print(f'{txt:^100} ')
    print('-'*100)


def cor(cor='n'):
    '''
    Formata a cor das letras conforme escolhido no parametro
    
    :param cor: Recebe o nome da cor escolhida por uma string, com padrão sem formatação
    '''
    if cor.lower() == 'verde':
        print('\033[32m')
    elif cor.lower() == 'vermelho':
        print('\033[31m')
    elif cor.lower() == 'cinza':
        print('\033[30m')
    elif cor.lower() == 'roxo':
        print('\033[34m')
    elif cor.lower() == 'rosa':
        print('\033[35m')
    elif cor.lower() == 'azul':
        print('\033[36m')
    elif cor.lower() == 'branco':
        print('\033[37m')
    elif cor.lower() == 'n':
        print('\033[m',end='')

