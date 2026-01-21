import requests

try:
    url = 'https://www.pudim.com.br/'
    resposta = requests.get(url, timeout=5)

except requests.exceptions.RequestException:
    print('\033[31mO site não está acessivel no momento por favor tente mais tarde...\033[m ')

else:
    if resposta.status_code == 200:
        print('\033[32mO site está acessivel no momento...\033[m ')
    elif resposta.status_code == 404:
        print('\033[31mA URL fornecida não foi encontrada.\033[m ')
    elif resposta.status_code == 500:
        print('\033[31mAlgum erro interno no momento, por favor tente mais tarde.\033[m ')
    elif resposta.status_code == 403:
        print('\033[31mO acesso ao site foi negado.\033[m ')
    else:
        print(f'\033[31mAlgum erro inesperado cod_error: {resposta.status_code}\033[m ')
