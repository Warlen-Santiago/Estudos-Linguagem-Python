num = str(input('Insira um número qualquer de 0 - 9999 para ver suas casas separadamente: '))

numsep = list(num)

num_qunt = len(num)

if num_qunt == 4:
    print(f'Casa das unidades: {numsep[0]}\nCasa das dezenas: {numsep[1]}\nCasa das centenas: {numsep[2]}\nCasa do unidade de milhar: {numsep[3]} ')
elif num_qunt == 3:
    print(f'Casa das unidades: {numsep[0]}\nCasa das dezenas: {numsep[1]}\nCasa das centenas: {numsep[2]} ')
elif num_qunt == 2:
    print(f'Casa das unidades: {numsep[0]}\nCasa das dezenas: {numsep[1]} ')
elif num_qunt == 1:
    print(f'Casa das unidades: {numsep[0]} ')
else:
    print('Insira um valor valido e tente novamente! ')
