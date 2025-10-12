print('='*40)
print(f'{'BANCO AC':^38}')
print('='*40)

'''Recendo valor que o usuario deseja sacar'''
valor = int(input('Insira o valor que deseja sacar: '))

'''uma listagem com as notas disponiveis sendo indexadas da seguinte forma: [0] = representa notas de 50, [1] = de 20, [2] = de 10, [3] = de 1 '''
notas_disponiveis = (50, 20, 10, 1)
'''lista para armazenar quantas notas vão ser retiradas de cada, iniciada em zero pois o calculo ainda não foi feito'''
n = [0, 0, 0, 0]

'''contador é essencial, sera dividido em 4 etapas pois são quatro variações de cedulas disponiveis '''
cont=0
while True:
    '''começamos sabendo quantas cedulas serão do maior valor como indexado nas listagens acima'''
    n[cont] = valor // notas_disponiveis[cont]
    '''depois atualizamos o valor para que receba o valor descontado das cedulas que ja foram contadas, assim quando o ciclo se repitir o valor estara atualizado conforme a necessidade'''
    valor -= notas_disponiveis[cont] * n[cont]

    cont+=1
    if cont == 4:
        break
print('='*40)

print('Serão liberadas as seguintes cedulas:')
print(f'''R$ 50: {n[0]}
R$ 20: {n[1]}
R$ 10: {n[2]}
R$ 1: {n[3]}''')
