print('Vamos saber se com 3 retas você consegue formar um triangulo: ')

a = float(input('Reta A: '))
b = float(input('Reta B: '))
c = float(input('Reta C: '))

if a + b > c and a + c > b and b + c > a:
    print('Você tem um triangulo! ')
    if a == b and a == c and b ==c:
        print('E ele é um triangulo Equilátero! ')
    elif a == b or a == c or c == b:
        print('E ele é um triangulo Isósceles! ')
    else:
        print('E ele é um triangulo Escaleno! ')
else:
    print('Você não tem um triangulo! ')
