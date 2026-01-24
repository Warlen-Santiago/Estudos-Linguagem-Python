import json #permite o trabalho dentro do codigo com arquivos .json
import os #confere se o arquivo existe 


def carrega(arquivo):
    '''
    Verifica a existencia de um arquivo.json, se o arquivo existir ele o carrega, caso não exista ele cria e retorna uma lista vazia
    
    :param arquivo: Recebe o caminho e ou nome do arquivo que deseja verificar/abrir
    '''
    try:
        if os.path.exists(arquivo):
            with open(arquivo, 'r', encoding='utf-8') as f:
                pessoas = json.load(f)
        else:
            pessoas = []

        return pessoas
    except json.JSONDecodeError:
        print('O arquivo informado no codigo não se trata de um arquivo .json, favor corrigir e tentar novamente... ')


def salva(arquivo, dados=()):
    '''
    Recebe dados de uma lista/tupla/dicionario e salva em um arquivo .json
    
    :param arquivo: Nome do arquivo existente ou do que sera criado
    :param dados: Dados de tupla/lista/dicionario que serão salvos
    '''

    try:
        with open(arquivo,'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4 )
    except FileNotFoundError:
        print('Erro no caminho fornecido...')
    except:
        print('Algo deu errado, tente novamente... caso erro persista entre em contato com suporte. ')
    else:
        print('\033[32mDados salvos!\033[m')
        
