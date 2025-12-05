import datetime

def idade(ano_de_nascimento):
    '''
    Docstring para idade
        A função recebe o ano de nascimento, coleta o ano atual
        e retorna a idade calculada com os dois fatores
    :param ano_de_nascimento: recebe o ano de nascimento
    '''
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_de_nascimento

    return idade