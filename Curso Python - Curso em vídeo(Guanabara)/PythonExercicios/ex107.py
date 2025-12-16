import moeda
import validação_escolhida


valor = int(input('Insira um valor: '))

print('-'*30)
print(f'{'SELECIONE UMA OPERAÇÃO':^30}')
print('-'*30)

while True:
    escolha = validação_escolhida.valida('''
            1 - Aumentar
            2 - Diminur
            3 - Dobrar
            4 - Metade
            5 - Novo Valor\n''',(1,2,3,4,5))
    print('-'*30)

    if escolha == 1:
        p = int(input(f'Em quanto por cento você quer aumentar {valor}? '))
        print(f'{valor} aumentado em {p}% fica : {moeda.aumentar(valor,p)}. ')
    elif escolha == 2:
        p = int(input(f'Em quanto por cento você quer diminuir {valor}? '))
        print(f'{valor} reduzido em {p}% fica: {moeda.diminuir(valor,p)}. ')
    elif escolha == 3:
        print(f'O dobro de {valor} é {moeda.dobro(valor)}. ')
    elif escolha == 4:
        print(f'A metade de {valor} é {moeda.metade(valor)}. ')
    elif escolha == 5:
        valor = int(input('Insira o novo valor desejado: '))

    print('-'*30)
    escolha = validação_escolhida.valida('Deseja contonuar?[S/N] ',('N','S'))

    if escolha == 'N':
        break
