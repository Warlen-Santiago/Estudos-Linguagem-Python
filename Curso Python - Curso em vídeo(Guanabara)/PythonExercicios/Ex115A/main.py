from lib import estruct, manipulação
from time import sleep

arq = 'cadastro.txt'

if not manipulação.arqexist(arq):
    manipulação.criararq(arq)

while True:
    escolha = estruct.menu(('Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair Do Sitema'))
    
    if escolha == 1:
        
        manipulação.lerarq(arq)

    elif escolha == 2:
        estruct.cabeçalho('CADASTRANDO PESSOA:')
        nome = input('Nome: ')
        idade = estruct.validaint('Idade: ')
        manipulação.cadastrar(arq, nome, idade)
        

    elif escolha == 3:
        estruct.cabeçalho('\033[30mSaindo do sitema... volte sempre!\033[m ')
        break
    else:
        print('\033[;31mError... Escolha uma opção valida e tente novamente.\033[m  ')
    sleep(2)