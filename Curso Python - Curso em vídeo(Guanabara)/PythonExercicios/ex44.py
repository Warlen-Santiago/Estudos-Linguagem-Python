valor = float(input('Insira o valor do produto: '))

fdp = int(input('Escolha a forma de pagamento:\n 1-A vista no Dinheiro/Pix/Cheque (10% de desconto)\n 2-Debito (5% de desconto)\n 3-Até 2x no credito (sem juros)\n 4-3x ou mais no credito (20% de juros)\n '))

if fdp == 1:
    print(f'O valor com 10% de desconto é R${valor-(valor*0.10):.2f}. ')
elif fdp == 2:
    print(f'O valor com 5% de desconto é R${valor-(valor*0.05):.2f}. ')
elif fdp == 3:
    print(f'O valor é {valor}. ')
elif fdp == 4:
    print(f'O valor com 20% de juros é R${valor+(valor*0.20):.2f}. ')
else:
    print('Insira uma escolha valida e tente novamente. ')
