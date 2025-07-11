num = str(input('Insira um número qualquer de 0 - 9999 para ver suas casas separadamente: '))

num_qunt = len(num)

if num_qunt == 4:
    print(f'Casa das unidades: {num[0]}\nCasa das dezenas: {num[1]}\nCasa das centenas: {num[2]}\nCasa do unidade de milhar: {num[3]} ')
elif num_qunt == 3:
    print(f'Casa das unidades: {num[0]}\nCasa das dezenas: {num[1]}\nCasa das centenas: {num[2]} ')
elif num_qunt == 2:
    print(f'Casa das unidades: {num[0]}\nCasa das dezenas: {num[1]} ')
elif num_qunt == 1:
    print(f'Casa das unidades: {num[0]} ')
else:
    print('Insira um valor valido e tente novamente! ')
