km = float(input('Insira a distancia da viagem em km. '))

if km <= 200:
    print(f'O custo da viagem será de R${km*0.50:.2f}. ')
else:
    print(f'O custo da viagem será de R${km*0.45:.2f}. ')
