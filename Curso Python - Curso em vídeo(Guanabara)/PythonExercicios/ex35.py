print('Vamos saber se com 3 retas você consegue formar um triangulo: ')

a = float(input('Reta A: '))
b = float(input('Reta B: '))
c = float(input('Reta C: '))

if a + b > c and a + c > b and b + c > a:
    print('Você tem um triangulo! ')
else:
    print('Você não tem um triangulo! ')
