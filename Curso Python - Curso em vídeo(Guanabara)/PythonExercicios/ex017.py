from math import hypot
print('Calculando a Hipotenusa de um triângulo retângulo: ')
cat_op = float(input('Insira o cateto oposto:\n '))
cat_ad = float(input('Insira o cateto adjacente:\n '))
print(f'O valor da Hipotenusa desse triângulo é de {hypot(cat_op, cat_ad):.2f} ')
