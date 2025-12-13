from time import sleep

cores ={
    'sem cor' : '\033[m',
    'vermelho' : '\033[0;30;41m',
    'verde' : '\033[0;30;42m',
    'amarelo' : '\033[0;30;43m',
    'azul' : '\033[0;30;44m',
    'roxo' : '\033[0;30;45m',
    'branco' : '\033[7;30m',
}

def ajuda(cod):

    print(help(cod))

def titulo(txt, cor='sem cor'):
    q = len(txt)+2
    print(cores[cor],'-'*q)
    print(f' {txt}  ')
    print('','-'*q,cores['sem cor'])

while True:
    sleep(1)
   
    titulo('SISTEMA DE AJUDA PYTHON','verde')

    escolha = input('Sobre qual função ou biblioteca deseja consultar? - [Digite (fim) para encerrar]' ).lower()
    
    if escolha == 'fim':
        titulo('ENCERRANDO PROGRAMA... VOLTE SEMPRE!', 'vermelho')
        sleep(1)
        break
    else:
        titulo(f'CONSULTANDO BASE HELP PYTHON COMANDO: {escolha}', 'azul')
        sleep(1)
        print(cores['branco'])
        ajuda(escolha)
        print(cores['sem cor'])
 