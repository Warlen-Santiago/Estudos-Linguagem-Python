v = int(input('Insira a velocidade do veículo '))

if v > 80:
    print(f'Foi multado, o valor da multa é de R${(v - 80)*7}. ')
else:
    print('Você não foi multado, continue obedecendo as leis de transito ')
