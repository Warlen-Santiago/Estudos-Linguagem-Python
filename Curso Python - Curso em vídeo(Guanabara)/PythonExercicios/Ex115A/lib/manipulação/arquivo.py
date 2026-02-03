from lib.estruct import interface


def arqexist(arq):
    try:
        f = open(arq, '+rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criararq(arq):
    try:
        f = open(arq, 'wt+', encoding='utf-8')
        f.close()
    except:
        print('Houve algum erro na criação do arquivo. ')
    else:
        print(f'Arquivo {arq} criado com sucesso. ')


def lerarq(arq):
    try:
        f = open(arq, 'rt', encoding='utf-8')    
    except:
        print('Erro ao ler arquivo... ')
    else:
        interface.cabeçalho('PESSOAS CADASTRADAS')
        for linha in f:
            dados_separados = linha.split(';')
            dados_separados[1] = dados_separados[1].replace('\n', '')
            print(f'{dados_separados[0]:<30} {dados_separados[1]} anos')
    finally:
        f.close()


def cadastrar(arq, nome='Não adicionaado', idade=00):
    try:
        f = open(arq, 'at', encoding='utf-8')
    except:
        print('Houve um erro na abertura do arquivo. ')
    else:
        try:
            f.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na adição de novos dados. ')
        else:
            print(f'novo registro de {nome} adicionado')