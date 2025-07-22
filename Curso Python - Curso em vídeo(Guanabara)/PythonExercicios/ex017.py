from math import hypot
print('Calculando a Hipotenusa de um triângulo retângulo: ')
cat_op = float(input('Insira o \033[1;37mcateto oposto\033[m:\n '))
cat_ad = float(input('Insira o \033[1;37mcateto adjacente\033[m:\n '))
print(f'O valor da Hipotenusa desse triângulo é de {hypot(cat_op, cat_ad):.2f} ')
