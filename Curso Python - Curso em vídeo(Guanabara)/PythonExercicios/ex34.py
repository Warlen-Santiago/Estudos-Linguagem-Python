sal = float(input('Insira o salário para ver seu aumento: '))

if sal > 1250:
    print(f'O sálario com aumento fica R${sal+sal*0.10} ')
else:
    print(f'O sálario com aumento fica R${sal+sal*0.15} ')
