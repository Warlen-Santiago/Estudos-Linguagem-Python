import datetime

def voto(ano_de_nascimento):
    '''
    Docstring para idade
        A função recebe o ano de nascimento, coleta o ano atual
        calculada a idade  com os dois fatores e verifica a obrigatoriedade do voto da pessoa
    :param ano_de_nascimento: recebe o ano de nascimento
    '''
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_de_nascimento

    if idade <16:
        print(f'Com {idade} anos, Menores de 16 anos NÃO VOTAM. ')
    elif idade >= 16 and idade < 18:
        print(f'Com {idade} anos, Menores de 18 anos e maiores de 16 tem voto OPICIONAL. ')
    elif idade >= 18 and idade <60:
        print(f'Com {idade} anos, Maiores de 18 anos que ainda não completaram 60 anos tem voto OBRIGATÓRIO. ')
    elif idade >= 60:
        print(f'Com {idade} anos, Maiores de 60 anos tem voto OPICIONAL. ')
    
print('Obrigatoriedade do voto: ')

a = int(input('-Insira seu ano de nascimento: \n'))
voto(a)
