print('Aluguel de carros.' )
dias = int(input('De quantos dias foi o aluguel do carro?\n' ))
km = float(input('Quantos km foram percorridos com o carro?\n' ))
vt = dias * 60 + km * 0.15
print(f'O valor a ser pago é de R${vt:.2F}' )