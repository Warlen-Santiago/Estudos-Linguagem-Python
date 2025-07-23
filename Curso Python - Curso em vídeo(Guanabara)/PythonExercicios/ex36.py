print('Simulação de empréstimo Bancário Imobiliário ')

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual salario do comprador? '))
tempo_pagamento = int(input('Em quantos anos ele pretende pagar o emprestimo? '))

if (salario * 0.30) >= (valor_casa / (tempo_pagamento * 12)):
    print('Emprestimo aprovado! ')
else:
    print('Eemprestimo negado! ')
