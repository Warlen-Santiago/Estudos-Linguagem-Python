'''Inicializando as variaveis'''
escolha = 0
contador = 1

'''Laço de repetição'''
while escolha != 5:
    '''verificando se a necessidade de entrada de dados(por inicio ou por escolha do usuario)'''
    if contador == 1:
        n1 = float(input('Insira o 1° valor: '))
        n2 = float(input('Insira o 2° valor: '))
    elif escolha == 4:
        n1 = float(input('Insira o 1° valor: '))
        n2 = float(input('Insira o 2° valor: '))

        '''tabela com opções para escolha'''
    print('''
        [1]- SOMA
        [2]- MULTIPLICAR
        [3]- MAIOR
        [4]- NOVOS NÚMEROS
        [5]- FECHAR PROGRAMA
    ''')

    '''Escolha do usuario'''
    escolha = int(input('Selecione uma das opções a cima: '))

    '''resoluções de acordo com a escolha'''
    if escolha == 1:
        print(f'A soma de {n1:.2f} e {n2:.2f} é {n1+n2:.2f}. ')
    elif escolha == 2:
        print(f'A multiplicação de {n1:.2f} por {n2:.2f} é {n1*n2:.2f}. ')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1:.2f} é maior que {n2:.2f}. ')
        elif n2 > n1:
            print(f'{n2:.2f} é maior que {n1:.2f}. ')
        else:
            print('Os valores inseridos são iguais. ')

    '''Garantia de que os valores númericos serão pedidos somente quando o programa iniciar ou por escolha do usuario'''
    contador += 1
print('Programa encerrado.')
